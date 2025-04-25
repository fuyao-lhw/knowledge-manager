"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/18 14:26
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  documents_tagsService.py

功能描述

实现步骤

"""
from perKnowManage.mapper.documents_tagsMapper import (
    select_documentId_by_tagId, add_did_tid)
from perKnowManage.config import logger


# 添加document_id和tag_id
def add_did_tid_service(document_id, tag_id):
    """添加document_id和tag_id"""
    # 查询标签id对应的文档id,如果已经存在标签id,就说明已经添加过,不需要在添加
    try:
        d_ids = select_documentId_by_tagId(tag_id)
        if document_id not in d_ids:  # 如果document_id不在查询的标签id对应的文档id的列表内,说明没有添加过
            add_did_tid(document_id, tag_id)
            logger.info(f"文档{document_id}与标签{tag_id}对应成功!")
        else:
            logger.info(f"文档{document_id}与标签{tag_id}已经对应")
    except AttributeError:  # 标签id没有对应文档id,可以直接添加
        add_did_tid(document_id, tag_id)
        logger.info(f"文档{document_id}与标签{tag_id}对应成功!")



