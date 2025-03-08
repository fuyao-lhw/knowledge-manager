"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/3/8 17:31
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  get_documents_list.py

功能描述

实现步骤

"""
from datetime import datetime

from perKnowManage.Models.models import Documents
import os
from perKnowManage.config import FILE_FOLDER


class DocumentList:
    def __init__(self, form):
        """
        从数据库-文档表 获取数据
        :param form: 获取形式 latest:获取最新的五条数据,展示在首页; all:由于未部署,无服务器,暂不开放功能
        :return:
        """
        self.form = form

    # 从数据库获取
    def from_db(self):

        if self.form == "latest":
            documents = Documents.query.order_by(Documents.upload_time.desc()).limit(5).all()
            result = [
                {
                    "title": d.title,  # 文档标题
                    "upload_time": "d.uplpad_time",  # 上传时间
                    "user_id": d.user_id,  # 用户id
                } for d in documents
            ]
            return result
        elif self.form == "all":
            print("暂未开放")

    def from_folder(self):
        file_list = os.listdir(FILE_FOLDER)
        file_info = []

        for filename in file_list:
            file_path = os.path.join(FILE_FOLDER, filename)

            # 排除目录只处理文件
            if os.path.isfile(file_path):
                stat_info = os.stat(file_path)

                file_info.append({
                    "name": filename,  # 文件名
                    "size": f"{round(stat_info.st_size / 1024, 2)} KB",  # 转换为KB单位
                    "upload_time": datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')  # 格式化修改时间
                })
        # print(file_info)

        if self.form == "latest":
            # 按修改时间倒序排序并取前5个
            sorted_files = sorted(file_info,
                                  key=lambda x: x["upload_time"],
                                  reverse=True)[:5]
            print(sorted_files)
            return sorted_files
        elif self.form == "all":
            print("暂未开放")
