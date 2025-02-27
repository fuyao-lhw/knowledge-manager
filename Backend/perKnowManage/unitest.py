"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/2/27 21:07
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  unitest.py

功能描述

实现步骤

"""
from datetime import datetime

from perKnowManage.Models.models import Users
from perKnowManage.config import db

def test():
    # 创建用户时传入 datetime 对象
    new_user = Users(
        email="2704316524@qq.com",
        password="lhw050727",
        created_at=datetime.now(),  # 直接传入 datetime 对象
        login_ts=datetime.now()
    )
    db.session.add(new_user)
    db.session.commit()
