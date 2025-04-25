"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/17 0:07
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  documents_tagsMapper.py

功能描述

实现步骤

"""
from perKnowManage.config import db, logger
from perKnowManage.pojo.models import document_tags


def select_documentId_by_tagId(tag_id):
    """根据标签id查询文档id"""
    dts = db.session.query(document_tags).filter_by(tag_id=tag_id).all()
    return [d.document_id for d in dts]  # 返回该标签对应的所有id,因为可能一个标签对应多个文档


def add_did_tid(document_id, tag_id):
    """添加document_id和tag_id"""
    new_dts = document_tags.insert().values(document_id=document_id, tag_id=tag_id)  # 插入
    db.session.execute(new_dts)
    db.session.commit()
    # return new_dts.id


def select_all_documentId_by_tag_id(tag_id):
    """根据标签id获取所有的文档id"""
    dts = db.session.query(document_tags).filter_by(tag_id=tag_id).all()
    # db.session.execute(dts)
    return dts

def delete_by_did_tid(document_id, tag_id):
    """根据文档id和标签id删除表中的数据"""
    dts = document_tags.delete().filter_by(document_id=document_id, tag_id=tag_id)
    db.session.execute(dts)
    db.session.commit()
