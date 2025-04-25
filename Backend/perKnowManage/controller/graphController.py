"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/22 10:25
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  graphController.py

功能描述

实现步骤

"""
from flask import Blueprint
from perKnowManage.config import logger
from perKnowManage.service.graphService import get_relation_service

bp = Blueprint("graph", __name__)


@bp.route("/graph/data", methods=["GET"])
def graph_data():
    logger.info(f"获取图数据")
    return get_relation_service()
