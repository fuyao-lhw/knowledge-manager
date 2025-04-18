"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/16 0:14
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  tagsMapper.py

功能描述

实现步骤

"""
from perKnowManage.config import db, logger
from perKnowManage.pojo.models import Tags


def select_tag_id_by_tag(tag_name):
    """根据标签获取标签id"""
    tag = Tags.query.filter_by(name=tag_name).first()
    return tag.id

def select_tag_by_id(tag_id):
    """根据id获取标签"""


def get_all_tags():
    """获取所有标签"""
    tags = Tags.query.all()
    return tags


def update_tag(tag_id, tag_name):
    """更新标签"""
    tag = Tags.query.filter_by(id=tag_id).first()  # 查询
    tag.name = tag_name  # 更改标签名
    db.session.commit()  # 提交
    logger.error(f"标签更新发生错误:\n 标签id: {tag_id}; 标签名: {tag_name}")


def delete_tags(tag_id):
    """删除标签"""
    tag = Tags.query.filter_by(id=tag_id).first()
    db.session.delete(tag)  # 删除
    db.session.commit()


def add_tag(tag_name, user_id):
    """新增标签"""
    new_tag = Tags(name=tag_name, user_id=user_id)
    db.session.add(new_tag)
    db.session.commit()
    logger.info(f"新增标签的id: {new_tag.id}")
    return new_tag.id
