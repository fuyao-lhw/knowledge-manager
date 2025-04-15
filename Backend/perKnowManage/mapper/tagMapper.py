"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/16 0:14
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  tagMapper.py

功能描述

实现步骤

"""
from perKnowManage.config import db
from perKnowManage.pojo.models import Tags


def select_tag_id_by_tag(tag):
    """根据标签获取标签id"""
    tag = Tags.query.filter_by(tag=tag).first()
    return tag.id

