"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/15 22:58
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  result.py

功能描述

实现步骤

"""
from flask import jsonify


class Result:
    """标准化输出"""

    def __init__(self, data=None, msg=None):
        self.data = data
        self.msg = msg

    def fail(self):
        """失败"""
        self.msg = self.msg if self.msg else "error"
        return jsonify({
            "status": 100,
            "msg": self.msg,
            "data": self.data,
        })

    def success(self):
        """成功"""
        self.msg = self.msg if self.msg else "success"
        return jsonify({
            "status": 200,
            "msg": self.msg,
            "data": self.data,
        })
