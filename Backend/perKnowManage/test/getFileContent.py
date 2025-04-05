"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/3/31 14:42
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  getFileContent.py

功能描述

实现步骤

"""
import os
from perKnowManage.config import FILE_FOLDER



def get_file_list():
    # 获取所有条目
    all_entries = os.listdir(FILE_FOLDER)

    # 过滤掉文件夹（仅保留文件）
    file_list = [
        entry for entry in all_entries
        if os.path.isfile(os.path.join(FILE_FOLDER, entry))
    ]

    return file_list


def get_file_content(file_path):
    with open(fr"{file_path}", "r", encoding="utf-8") as f:
        content = f.read()

    return content

