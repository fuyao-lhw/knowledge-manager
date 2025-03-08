"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/3/8 17:31
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  get_documents_list.py

功能描述

实现步骤

"""
from perKnowManage.Models.models import Documents

# 从数据库获取
def get_documents_from_db(form):
    """
    从数据库-文档表 获取数据
    :param form: 获取形式 latest:获取最新的五条数据,展示在首页; all:由于未部署,无服务器,暂不开放功能
    :return:
    """
    if form == "latest":
        documents = Documents.query.order_by(Documents.upload_time.desc()).limit(5).all()
        result = [
            {
                "title": d.title,
                "":""
            } for d in documents
        ]