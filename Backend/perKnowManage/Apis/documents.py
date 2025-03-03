"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/2/26 13:55
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  documents.py

功能描述

实现步骤

"""
from flask import Blueprint, request
from perKnowManage.config import logger

bp = Blueprint("documents", __name__)

@bp.route("/documents", methods=["POST", "GET"])
def documents():
    if request.method == "POST":
        logger.info("上传文件")
