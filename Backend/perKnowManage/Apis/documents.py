"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/2/26 13:55
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  documents.py

功能描述

实现步骤

"""
import datetime

from flask import Blueprint, request, jsonify
from perKnowManage.config import logger, data_save_type, FILE_FOLDER
from perKnowManage.utils.documents import (
    DocumentList, DocumentsStatsInfo, DocumentDetail, DocumentToMySQL)
import os

bp = Blueprint("documents", __name__)


@bp.route("/documents", methods=["POST", "GET"])
def documents():
    if request.method == "POST":
        logger.info("上传文件接口")
        if "file" not in request.files:
            logger.info("未接收到文件!")
            return jsonify({
                "status": 100,
                "message": "没有文件"
            })

        # 获取用户
        data = request.form  # 获取附带参数
        username = data.get("username")  # 获取发送者的用户名

        # 文件操作
        file = request.files["file"]  # 获取文件
        file_content = file.read().decode("utf-8")  # 文件内容
        # print(file_content)  # 读取文件内容
        filename = file.filename
        save_path = os.path.join(FILE_FOLDER, filename)
        # file.save(save_path)
        logger.info(f"发送者: {username}; 文件保存至: {save_path}")
        logger.info(f"{file.filename}保存成功!")

        # 入库
        title = filename.title()  # 文档标题
        file_path = save_path  # 文件路径
        file_type = title.split('.')[-1]  # 文件类型
        user_id = username  # 上传用户
        logger.info(f"标题:{title},路径:{file_path},类型:{file_type},用户:{user_id}")
        dtm = DocumentToMySQL()
        dtm.save_to_mysql(title, file_path, file_type, user_id)
        logger.info("数据添加成功!")

        return jsonify({
            "status": 200,
            "message": "上传成功"
        })

    if request.method == "GET":
        logger.info("文档列表接口")
        data = request.args
        get_form = data["form"]
        logger.info(f"请求形式:{get_form}")
        document_list = DocumentList(form=get_form)
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
        return jsonify({
            "status": 200,
            "message": "获取成功",
            "data": result
        })


@bp.route("/stats", methods=["GET", "POST"])
def stats():
    if request.method == "GET":
        logger.info("读取数据展示信息")
        documents_info = DocumentsStatsInfo()
        result = []
        # 数据库
        if data_save_type == 0:
            result = documents_info.db_info()
        # 本地
        if data_save_type == 1:
            result = documents_info.folder_info()
        logger.info(f"stats, {result}")
        return jsonify({
            "status": 200,
            "message": "获取成功",
            "data": result
        })


@bp.route("/document/<document_id>", methods=["POST", "GET"])
def get_documents_details(document_id):
    if request.method == "GET":
        logger.info("获取文档的详细信息")
        document_detail = DocumentDetail(document_id=document_id)
        result = document_detail.get_document_base_info()
        logger.info(result)
        return jsonify({
            "status": 200,
            "message": f"文章{document_id}获取成功;时间为:{datetime.datetime.now()}",
            "data": result,
        })
