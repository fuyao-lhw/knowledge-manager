"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/2/26 13:55
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  documentsMapper.py

功能描述

实现步骤

"""
from flask import Blueprint, request
from perKnowManage.config import logger
from perKnowManage.service.documentService import (
    get_document_list_service, get_document_detail, get_stats_service,
    upload_document_service, update_document_service
)

bp = Blueprint("documents", __name__)


# 文档上传方法
@bp.route("/documents", methods=["POST"])
def documents():
    if request.method == "POST":
        logger.info("上传文件接口")

        # 获取参数
        data = request.form  # 获取附带参数
        username = data.get("username")  # 获取发送者的用户名
        fileInfos = data.get("fileInfos")  # 文档信息
        fileList = request.files.getlist("files")  # 获取文件列表

        return upload_document_service(username, fileInfos, fileList)


# 获取文档列表
@bp.route("/documents", methods=["GET"])
def get_document_list():
    if request.method == "GET":
        logger.info("文档列表接口")
        data = request.args
        form = data["form"]
        logger.info(f"请求形式:{form}")
        return get_document_list_service(form)


# 更新文档
@bp.route("/documents/<document_id>", methods=["PUT"])
def update_documents(document_id):
    logger.info(f"文档更新接口: {document_id}")
    return update_document_service(document_id)


# 获取文档详细内容
@bp.route("/documents/<document_id>", methods=["GET"])
def get_documents_details(document_id):
    if request.method == "GET":
        logger.info("获取文档的详细信息")
        return get_document_detail(document_id)


@bp.route("/stats", methods=["GET", "POST"])
def stats():
    if request.method == "GET":
        logger.info("读取数据展示信息")
        return get_stats_service()
