"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/2/26 14:12
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  tagsController.py

功能描述

实现步骤

"""
from flask import Blueprint, request
from perKnowManage.config import logger
from perKnowManage.service.tagsService import (
    get_all_tags_service, update_tags_service, delete_tags_service, add_tag_service,
    select_all_document_by_tag_id_service
)

bp = Blueprint("tags", __name__)


# 获取标签列表
@bp.route("/tags", methods=["GET"])
def get_tags_list():
    """获取标签列表"""
    logger.info("获取标签列表")
    return get_all_tags_service()


# 更新标签
@bp.route("/tags", methods=["PUT"])
def update_tags():
    """批量更改标签"""
    logger.info("批量更改标签")
    data = request.get_json()  # 获取数据
    logger.info(data)
    tags = data["tagsData"]  # 获取需要更改的标签列表
    return update_tags_service(tags)


# 删除标签
@bp.route("/tags", methods=["DELETE"])
def delete_tags():
    """批量删除标签"""
    logger.info("批量删除标签")
    data = request.get_json()  # 获取数据
    logger.info(data)
    tags = data["tagsData"]
    return delete_tags_service(tags)


# 添加标签
@bp.route("/tags", methods=["POST"])
def add_tag():
    """添加标签"""
    logger.info("添加标签")
    data = request.get_json()  # 获取数据
    logger.info(data)
    tag_name, username = data["tag_name"], data["username"]  # 标签名和用户名
    return add_tag_service(tag_name, username)


# 根据标签id获取对应的文档列表
@bp.route("/tags/<tag_id>", methods=["GET"])
def get_documents_by_tag_id(tag_id):
    """获取文档标签对应的文档"""
    return select_all_document_by_tag_id_service(tag_id)