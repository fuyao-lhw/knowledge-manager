"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/25 21:35
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  graphMapper.py

功能描述

实现步骤

"""
from perKnowManage.mapper.tagsMapper import get_all_tags
from perKnowManage import create_app
from perKnowManage.pojo.models import Documents, Tags, document_tags
from perKnowManage.config import db


def get_relationship_between_document_and_tag():
    """查找具有共同标签的文档对"""
    # 为表创建别名
    dt1 = document_tags.alias()
    dt2 = document_tags.alias()
    doc1_table = Documents.__table__
    doc2_table = doc1_table.alias()

    # 执行查询
    results = db.session.query(
        doc1_table.c.id.label('doc1_id'),
        doc1_table.c.title.label('doc1_title'),
        doc2_table.c.id.label('doc2_id'),
        doc2_table.c.title.label('doc2_title'),
        Tags.name
    ).join(
        dt1, doc1_table.c.id == dt1.c.document_id
    ).join(
        Tags, dt1.c.tag_id == Tags.id
    ).join(
        dt2, Tags.id == dt2.c.tag_id
    ).join(
        doc2_table, dt2.c.document_id == doc2_table.c.id
    ).filter(
        doc1_table.c.id < doc2_table.c.id
    ).order_by(
        Tags.name
    ).all()

    return results
