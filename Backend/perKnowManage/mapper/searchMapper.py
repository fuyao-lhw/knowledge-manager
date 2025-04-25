"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/21 14:33
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  searchMapper.py

功能描述

实现步骤

"""
from perKnowManage.config import db, logger
from perKnowManage.pojo.models import Documents


def search_title(keyword):
    """模糊匹配"""
    documents = Documents.query.filter(Documents.title.ilike(f'%{keyword}%')).all()
    logger.info(f"查询结果: {documents}")

    return documents
