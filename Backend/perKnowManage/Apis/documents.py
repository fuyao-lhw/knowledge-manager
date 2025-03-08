"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/2/26 13:55
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  documents.py

功能描述

实现步骤

"""
from flask import Blueprint, request, jsonify
from perKnowManage.config import logger, data_save_type, FILE_FOLDER

bp = Blueprint("documents", __name__)


@bp.route("/documents", methods=["POST", "GET"])
def documents_upload():
    if request.method == "POST":
        logger.info("上传文件")
        if "file" not in request.files:
            return jsonify({
                "status": False,
                "message": "没有文件"
            })
        print(request.files)
        file = request.files["file"]
        # file.save(rf"E:\骆鸿威\{file.filename}")
        return jsonify({
            "status": True,
            "message": "上传成功"
        })


@bp.route("/documents", methods=["GET"])
def documents_list():
    if request.method == "GET":
        logger.info("文档列表接口")
        # 数据库方式
        if data_save_type == 0:
            pass