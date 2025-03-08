"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/2/26 13:04
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  config.py

功能描述

实现步骤

"""
# SQLAlchemy定义
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# 日志
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

# 验证码
verify_code_temp = ""

# 数据存储方式
"""
0:数据库存储
1:本地文件路径存储
"""
data_save_type = 1
# 本地文件存储路径
FILE_FOLDER = r"D:\code\All_Learning\MarkdownNotes"
