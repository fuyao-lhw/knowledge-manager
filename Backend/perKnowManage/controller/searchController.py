"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/21 14:22
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  searchController.py

功能描述
    处理搜索的接口
实现步骤

"""
from flask import Blueprint, request
from perKnowManage.config import logger
from perKnowManage.service.searchService import search_service

bp = Blueprint("search", __name__)


# 搜索接口
@bp.route("/search", methods=["POST"])
def search():
    logger.info("搜索接口")
    data = request.get_json()  # 数据
    logger.info(data)
    keyword = data["keyword"]
    return search_service(keyword)
