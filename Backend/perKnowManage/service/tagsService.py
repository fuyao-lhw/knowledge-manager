"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/16 15:02
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  tagsService.py

功能描述

实现步骤

"""
from perKnowManage.mapper.tagsMapper import (
    get_all_tags, update_tag, delete_tags, add_tag, select_tag_id_by_tag)
from perKnowManage.mapper.identityMapper import select_user_id_by_username
from perKnowManage.pojo.result import Result
from perKnowManage.config import logger
from perKnowManage.mapper.documents_tagsMapper import (
    select_all_documentId_by_tag_id
)
from perKnowManage.mapper.documentsMapper import (
    select_document_by_id
)


def get_all_tags_service():
    """获取所有标签的服务"""
    tags = get_all_tags()
    result = [{
        "tag_id": tag.id,  # 标签id
        "tag_name": tag.name,  # 标签名
        "user_id": tag.user_id,  # 用户id
    } for tag in tags]
    return Result(msg="获取成功", data=result).success()


def update_tags_service(tags):
    """更改标签列表"""
    error_tag_list = []  # 失败的列表
    for tag in tags:
        tag_id, tag_name = tag["tag_id"], tag["tag_name"]  # 标签id和标签名
        try:
            update_tag(tag_id=tag_id, tag_name=tag_name)
        except Exception as e:
            logger.error(f"标签更新发生错误({e}):\n 标签id: {tag_id}; 标签名: {tag_name}")
            error_tag_list.append(tag)

    return Result(
        msg=f"成功: {len(tags) - len(error_tag_list)}; 失败: {len(error_tag_list)}",
        data=error_tag_list
    ).success()


def delete_tags_service(tags):
    """批量删除标签"""
    error_tag_list = []  # 失败的列表
    for tag in tags:
        tag_id, tag_name = tag["tag_id"], tag["tag_name"]  # 标签id和标签名
        try:
            delete_tags(tag_id=tag_id)  # 删除
        except Exception as e:
            logger.error(f"标签删除发生错误({e}):\n 标签id: {tag_id}; 标签名: {tag_name}")
            error_tag_list.append(tag)

    return Result(
        msg=f"成功: {len(tags) - len(error_tag_list)}; 失败: {len(error_tag_list)}",
        data=error_tag_list
    ).success()


def add_tag_service(tag_name, username):
    """新增标签的服务"""
    user_id = select_user_id_by_username(username)  # 获取用户id
    try:
        tag_id = select_tag_id_by_tag(tag_name)  # 查询该标签是否存在
        logger.info(f"标签已经存在 --- {tag_name}: {tag_id}")
    except AttributeError as e:
        new_tag_id = add_tag(tag_name, user_id)
        return Result(msg="新增成功!", data={"tag_id": new_tag_id}).success()
    except Exception as e:
        logger.error(f"未知错误: {e}")
        return Result(msg="添加失败,请联系网站开发人员")


def select_all_document_by_tag_id_service(tag_id):
    """根据标签id获取所有的文档id"""
    dts = select_all_documentId_by_tag_id(tag_id)
    documents = [select_document_by_id(d.document_id) for d in dts]
    documents = [d[0] for d in documents]
    data = {
        "tag_id": tag_id,
        "documents_info": [
            {
                "id": d.id,
                "title": d.title,
                "update_time": d.update_time
            } for d in documents
        ]
    }
    return Result(msg=f"获取标签{tag_id}的对应文档列表成功!", data=data).success()
