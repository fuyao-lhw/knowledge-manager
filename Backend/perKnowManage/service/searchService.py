"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/21 14:31
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  searchService.py

功能描述

实现步骤

"""
from perKnowManage.config import logger
from perKnowManage.mapper.searchMapper import search_title
from perKnowManage.pojo.result import Result


def search_service(keyword):
    """搜索服务"""
    logger.info(f"搜索服务: {keyword}")
    documents = search_title(keyword)
    result = [
        {
            "id": d.id,
            "title": d.title,
            "file_tag": d.file_tag,
            "update_time": d.update_time,
            "user_id": d.user_id
        } for d in documents
    ]
    print(result)
    return Result(msg="查询成功!", data=result).success()
