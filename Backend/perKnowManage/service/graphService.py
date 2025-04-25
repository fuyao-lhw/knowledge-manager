"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/25 21:35
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  graphService.py

功能描述

实现步骤

"""
from perKnowManage.mapper.graphMapper import (
    get_relationship_between_document_and_tag)
from perKnowManage.pojo.result import Result
from perKnowManage.config import logger


def get_relation_service():
    """获取相同标签的文档对的服务"""
    relation = get_relationship_between_document_and_tag()

    links = [
        {
            "source": r.doc1_title,
            "target": r.doc2_title,
        } for r in relation
    ]

    # 用于去重的字典，键为节点 id，值为节点信息
    node_dict = {}
    for re in relation:
        # 添加 doc1 节点
        if re.doc1_id not in node_dict:
            node_dict[re.doc1_id] = {
                "category": re.doc1_id,
                "name": re.doc1_title,
            }
        # 添加 doc2 节点
        if re.doc2_id not in node_dict:
            node_dict[re.doc2_id] = {
                "category": re.doc2_id,
                "name": re.doc2_title,
            }

    # 将字典转换为节点列表
    nodes = list(node_dict.values())

    data = {"links": links, "nodes": nodes}
    return Result(msg="获取图数据成功!", data=data).success()

