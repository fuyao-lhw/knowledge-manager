"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/15 13:48
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  identityMapper.py

功能描述

实现步骤

"""
import time
from perKnowManage.pojo.models import Users
from perKnowManage.config import db, logger


# 根据用户名查询id
def select_user_id_by_username(username):
    """查询用户名对应的id"""
    logger.info(f"查询用户名对应的id: {username}")
    user = Users.query.filter_by(email=username).first()
    user_id = user.id
    logger.info(f"{username}: {user_id}")

    return user_id


def get_user(email):
    """获取当前email对应的用户"""
    return Users.query.filter_by(email=email).first()


def add_user(email, password):
    """添加新用户"""
    ts = int(time.time())  # 当前时间
    # 添加数据
    new_user = Users(email=email, password=password, created_at=ts, login_ts=ts)
    db.session.add(new_user)
    db.session.commit()
