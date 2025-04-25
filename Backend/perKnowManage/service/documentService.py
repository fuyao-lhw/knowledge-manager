"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/15 22:19
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  documentService.py

功能描述

实现步骤

"""
import datetime
import json
import os
from perKnowManage.config import logger, data_save_type, FILE_FOLDER
from perKnowManage.mapper.documentsMapper import (
    DocumentList, DocumentsStatsInfo, DocumentDetail, select_document_id_by_name,
    add_document, update_document, delete_document

)
from perKnowManage.mapper.identityMapper import select_user_id_by_username
from perKnowManage.pojo.result import Result
from perKnowManage.service.tagsService import add_tag_service
from perKnowManage.service.documents_tagsService import add_did_tid_service
from perKnowManage.mapper.tagsMapper import select_tag_id_by_tag
from perKnowManage.utils.syncDBData import sync


def upload_document_service(username, fileInfos, fileList):
    """文件上传服务"""
    global document_id

    # 返回结果
    data = {
        "upload_files": [],
        "update_files": [],
        "error_files": [],
    }

    fileInfosDict = json.loads(fileInfos)  # 解析元数据
    logger.info(f"元数据: {fileInfosDict}")

    # 文件个数
    fileNumber = len(fileInfosDict)

    # 用户id:
    user_id = select_user_id_by_username(username)

    # 失败的文档
    errorFileList = []

    # 遍历文件信息
    for i in range(fileNumber):

        # 文档操作
        fileInfo = fileInfosDict[i]  # 文档信息
        fileName = fileInfo["fileName"]  # 文档名字
        fileSize = fileInfo["fileSize"]  # 文档大小
        tag = fileInfo["tags"]
        fileTags = tag if tag else [fileName.split(".")[-1]]  # 文档标签
        file = fileList[i]  # 文档
        # fileContent = file.read().decode("utf-8")  # 文档内容
        fileSavePath = os.path.join(FILE_FOLDER, fileName)  # 文档保存路径
        try:
            # 入库-documents
            logger.info(f"将文档数据写入documents表")
            logger.info(f"标题:{fileName},路径:{fileSavePath},类型:{fileTags},用户:{user_id}")
            try:
                document_id = select_document_id_by_name(fileName)  # 添加
                logger.info(f"文档{fileName}已经存在,默认覆盖原文档 -- {document_id}: {fileName}")
                data["update_files"].append(fileInfo)  # 已经存在的文件-更新
                update_document(document_id=document_id, update_time=datetime.datetime.now())
                # file.save(fileSavePath)  # 覆盖
            except AttributeError:
                logger.info("该文档不存在,保存")
                # 文档信息入库
                document_id = add_document(title=fileName, file_path=fileSavePath, file_tag=tag,
                                           user_id=user_id, upload_time=datetime.datetime.now(),
                                           update_time=datetime.datetime.now())
                # file.save(fileSavePath)  # 文档保存
                logger.info(f"用户名: {username}; 用户id: {user_id}")
                logger.info(f"文档保存成功: {fileSavePath}")
                data["upload_files"].append(fileInfo)  # 成功上传的文件
            except Exception as e:
                logger.info(f"未知错误: {e}")
            logger.info("数据添加成功!")

            # 入表-tags;documents_tags
            logger.info(f"将标签列表数据写入标签表&将文档id和标签id一一对应")
            logger.info(f"文件名: {fileName}; 文档标签: {fileTags};")
            for t in fileTags:
                add_tag_service(tag_name=t, username=username)  # 添加标签表的数据
                logger.info(f"标签{t}添加成功!")
                # 添加document_tags数据
                tag_id = select_tag_id_by_tag(tag_name=t)  # 获取数据
                add_did_tid_service(document_id, tag_id)

            logger.info(f"文档{fileName}所有标签添加成功! --- 长度: {len(fileTags)}")
            logger.info(f"文档{fileName}和所有标签一一对应成功! --- 长度: {len(fileTags)}")

        except Exception as e:
            logger.error(f"文件上传服务出错,第{i}个文件: {e}")
            errorFileList.append(fileInfo)

    data["error_files"] = errorFileList  # 更新错误文件
    return Result(msg=f"成功上传: {len(data['upload_files'])}; "
                      f"成功更新: {len(data['update_files'])};"
                      f"上传失败: {len(data['error_files'])}",
                  data=data
                  ).success()


def get_document_list_service(form):
    """获取文档列表服务"""
    document_list = DocumentList(form=form)
    result = []
    # 数据库方式
    if data_save_type == 0:
        logger.info("从数据库读取数据")
        result = document_list.from_db()
    # 本地
    elif data_save_type == 1:
        logger.info("从本地文件夹读取数据")
        result = document_list.from_folder()
    logger.info(f"documents, {result}")
    return Result(msg="获取成功", data=result).success()


def update_document_service(documents):
    """更新文档服务"""
    errorList = []
    successList = []
    for document in documents:
        try:
            # 更新document表
            document["update_time"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # 针对英文进行大小写处理
            tags = document["file_tag"].split(",")
            tags = [t[0].upper()+t[1:] if t.isalpha() else t for t in tags]
            document["file_tag"] = ",".join(tags)  # 拼接
            new = update_document(document)
            successList.append({"id": new.id, "title": new.title, "file_tag": new.file_tag})
            # 更新文档标签表
            sync()
        except Exception as e:
            logger.error(f"出现错误{document['id']}: {e}")
            errorList.append(document)

    return Result(msg=f"更新成功:{len(successList)};更新失败:{len(errorList)}", data={
        "errorList": errorList,
        "successList": successList
    }).success()


def delete_documents_service(documents):
    """删除文档的服务"""
    errorList = []
    successList = []
    for document in documents:
        try:
            document_id = document["id"]  # id
            if delete_document(document_id):
                successList.append(document)
        except Exception as e:
            logger.error(f"文档{document['id']}发生错误: {e}")
            errorList.append(document)
    return Result(msg=f"删除成功:{len(successList)};删除失败:{len(errorList)}",
                  data={
                      "errorList": errorList,
                      "successList": successList
                  }).success()


def get_document_detail(document_id):
    document_detail = DocumentDetail(document_id=document_id)
    result = document_detail.get_document_base_info()
    logger.info("文档详细内容", result)
    return Result(msg=f"文章{document_id}获取成功;时间为:{datetime.datetime.now()}", data=result).success()


def get_stats_service():
    """获取系统概览的展示数据"""
    documents_info = DocumentsStatsInfo()
    result = []
    # 数据库
    if data_save_type == 0:
        result = documents_info.db_info()
    # 本地
    if data_save_type == 1:
        result = documents_info.folder_info()
    logger.info(f"stats, {result}")
    return Result(msg="获取成功", data=result).success()
