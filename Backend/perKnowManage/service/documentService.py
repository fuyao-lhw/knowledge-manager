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
    DocumentList, DocumentsStatsInfo, DocumentDetail, DocumentToMySQL)
from perKnowManage.mapper.identityMapper import select_user_id_by_username
from perKnowManage.pojo.result import Result


def upload_document_service(username, fileInfos, fileList):
    """文件上传服务"""
    fileInfosDict = json.loads(fileInfos)  # 解析元数据
    logger.info(f"元数据: {fileInfosDict}")

    # 创建对象
    dtm = DocumentToMySQL()

    # 用户id:
    user_id = select_user_id_by_username(username)

    # 遍历文件信息
    for i in range(len(fileInfosDict)):
        # 文档操作
        fileInfo = fileInfosDict[i]  # 文档信息
        fileName = fileInfo["fileName"]  # 文档名字
        fileSize = fileInfo["fileSize"]  # 文档大小
        tag = fileInfo["tags"]
        fileTags = tag if tag else fileName.split(".")[-1]  # 文档标签
        file = fileList[i]  # 文档
        # fileContent = file.read().decode("utf-8")  # 文档内容
        fileSavePath = os.path.join(FILE_FOLDER, fileName)  # 文档保存路径
        # file.save(fileSavePath)  # 文档保存
        logger.info(f"用户名: {username}; 用户id: {user_id}")
        logger.info(f"文档保存成功: {fileSavePath}")

        # 入库-documents
        logger.info(f"将文档数据写入documents表")
        logger.info(f"标题:{fileName},路径:{fileSavePath},类型:{fileTags},用户:{user_id}")
        # document_id = dtm.save_to_documents(fileName, fileSavePath, fileTags, user_id)  # 添加
        logger.info("数据添加成功!")

        # 入表-tags
        logger.info(f"将标签列表数据写入标签表")
        logger.info(f"文件名: {fileName}; 文档标签: {fileTags};")
        # tags_id_list = dtm.save_to_tags(fileTags, user_id)  # 添加
        #
        # # 入表-documents_tags
        logger.info(f"将文档id和标签id一一对应")
        # # dtm.save_to_documents_tags(document_id, fileTags)


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
