"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/19 16:38
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  updateModelByDict.py

功能描述

实现步骤

"""


def update_model_by_dict(instance, data):
    """通过字典来更新数据"""
    for key, value in data.items():
        if key != 'id' and hasattr(instance, key):
            setattr(instance, key, value)
    return instance
