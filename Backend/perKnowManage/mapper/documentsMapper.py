"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/3/8 17:31
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  documentsMapper.py

功能描述

实现步骤

"""
from datetime import datetime, timedelta
from perKnowManage.pojo.models import Documents, Tags, document_tags
from perKnowManage.config import db, logger
import os
from perKnowManage.config import FILE_FOLDER
from sqlalchemy import func, distinct
from perKnowManage.mapper.tagsMapper import select_tag_id_by_tag
from perKnowManage.utils.updateModelByDict import update_model_by_dict


class DocumentList:
    """获取全部文档"""

    def __init__(self, form):
        """
        从数据库-文档表 获取数据
        :param form: 获取形式 latest:获取最新的五条数据,展示在首页; all:由于未部署,无服务器,暂不开放功能
        :return:
        """
        self.form = form

    # 从数据库获取
    def from_db(self):
        documents = None
        if self.form == "latest":
            documents = Documents.query.order_by(Documents.upload_time.desc()).limit(5).all()

        elif self.form == "all":
            documents = Documents.query.order_by(Documents.upload_time.desc()).all()
        result = [
            {
                "title": d.title.split('.')[0],  # 文档标题
                "upload_time": self._convert_gmt_time(d.upload_time),  # 上传时间
                "user_id": d.user_id,  # 用户id
                "id": d.id,  # 文档id
                "file_tag": d.file_tag,  # 文档标签
            } for d in documents
        ]
        return result

    def from_folder(self):
        file_list = os.listdir(FILE_FOLDER)
        file_info = []

        for filename in file_list:
            file_path = os.path.join(FILE_FOLDER, filename)

            # 排除目录只处理文件
            if os.path.isfile(file_path):
                stat_info = os.stat(file_path)

                file_info.append({
                    "title": filename,  # 文件名
                    "size": f"{round(stat_info.st_size / 1024, 2)} KB",  # 转换为KB单位
                    "upload_time": datetime.fromtimestamp(stat_info.st_mtime).strftime('%Y-%m-%d %H:%M:%S')  # 格式化修改时间
                })
        # print(file_info)

        if self.form == "latest":
            # 按修改时间倒序排序并取前5个
            sorted_files = sorted(file_info,
                                  key=lambda x: x["upload_time"],
                                  reverse=True)[:5]
            # print(sorted_files)
            return sorted_files
        elif self.form == "all":
            print("暂未开放")

    def _convert_gmt_time(self, dt_str):
        """将 GMT 时间字符串转为标准格式"""
        from datetime import datetime
        try:
            # 解析原始格式
            dt_obj = datetime.strptime(dt_str, '%a, %d %b %Y %H:%M:%S GMT')
            # 转为目标格式
            return dt_obj.strftime('%Y-%m-%d %H:%M:%S')
        except (TypeError, ValueError):
            # 如果已经是 datetime 对象直接格式化
            if isinstance(dt_str, datetime):
                return dt_str.strftime('%Y-%m-%d %H:%M:%S')
            return dt_str  # 保底返回原始数据


class DocumentsStatsInfo:
    """获取文档基本信息,用于前端展示总数等信息"""

    def __init__(self):
        self.knowledge_counts = 0  # 知识库总量
        self.tags_counts = 0  # 查询标签表的所有内容-->文档库总数
        self.document_counts = 0  # 查询文档列表的所有文档-->文档总量
        self.week_new_counts = 0  # 本周新增
        self.upload_user_counts = 0  # 文档上传成员

    # 在 DocumentsInfo 类中添加以下方法
    def _weekly_new_count(self):
        """统计本周新增文档数量"""
        # 获取当前时间
        now = datetime.now()

        # 计算本周开始时间（周一00:00）
        start_of_week = now - timedelta(days=now.weekday())
        start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)

        # 计算本周结束时间（下周一00:00）
        end_of_week = start_of_week + timedelta(days=7)

        # 查询本周新增数量
        count = Documents.query.filter(
            Documents.upload_time >= start_of_week,
            Documents.upload_time < end_of_week
        ).count()

        return count

    def db_info(self):
        """从数据库获取数据"""
        # 知识库总量
        self.knowledge_counts = 0
        # 查询标签表的所有内容-->文档库总数
        self.tags_counts = Tags.query.count()
        # 查询文档列表的所有文档-->文档总量
        self.document_counts = Documents.query.count()
        # 本周新增
        self.week_new_counts = self._weekly_new_count()
        # 文档上传成员
        self.upload_user_counts = Documents.query.with_entities(func.count(distinct(Documents.user_id))).scalar()

        result = [
            {"title": "知识库库总数", "value": self.knowledge_counts},
            {"title": "文档库总数", "value": self.tags_counts},
            {"title": "文档总量", "value": self.document_counts},
            {"title": "本周新增", "value": self.week_new_counts},
            {"title": "文档上传成员", "value": self.upload_user_counts},
        ]

        return result

    def folder_info(self):
        """统计本地文件信息"""
        file_list = os.listdir(FILE_FOLDER)

        # 计算本周时间范围 (复用已有逻辑)
        now = datetime.now()
        start_of_week = now - timedelta(days=now.weekday())
        start_of_week = start_of_week.replace(hour=0, minute=0, second=0, microsecond=0)
        end_of_week = start_of_week + timedelta(days=7)

        # 初始化计数器
        total_count = 0
        weekly_count = 0

        for filename in file_list:
            file_path = os.path.join(FILE_FOLDER, filename)
            if os.path.isfile(file_path):
                total_count += 1
                # 获取文件修改时间
                m_time = datetime.fromtimestamp(os.stat(file_path).st_mtime)
                # 判断是否在本周范围内
                if start_of_week <= m_time < end_of_week:
                    weekly_count += 1

        # 更新统计结果
        self.document_counts = total_count
        self.week_new_counts = weekly_count
        self.tags_counts = 8  # 保留原有逻辑
        self.upload_user_counts = 2  # 本地模式无用户信息

        result = [
            {"title": "知识库库总数", "value": self.knowledge_counts},
            {"title": "文档库总数", "value": self.tags_counts},
            {"title": "文档总量", "value": self.document_counts},
            {"title": "本周新增", "value": self.week_new_counts},
            {"title": "文档上传成员", "value": self.upload_user_counts},
        ]

        print("folder", result)
        return result


class DocumentDetail:
    """获取文档内容,用于前端文档展示"""

    def __init__(self, document_id):
        self.document_id = document_id
        self.result = {}

    def _query_document_base_info(self):
        """查询文档路径"""
        document = Documents.query.filter_by(id=self.document_id).first()
        self.result = {
            "title": document.title,
            "file_path": document.file_path,
        }
        return self.result

    def get_document_content(self):
        # result = self._query_document_base_info()
        file_path = self.result["file_path"]
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        html = content
        # if ".md" in file_path:
        #     # 证明是md文件
        #     html = mistune.markdown(content)

        return html

    def _link_to_url(self, content):
        image_regex = "!(\[\S+\])\(\S+\)"
        result = content.replace("images", "D:\code\All_Learning\MarkdownNotes\images")
        return result

    def get_document_base_info(self):
        """获取文档基本信息"""
        result = self._query_document_base_info()
        content = self.get_document_content()
        result["content"] = content

        return result


# 根据文档名查询文档id
def select_document_id_by_name(title):
    """根据文档名查询文档id"""
    document = Documents.query.filter_by(title=title).first()

    return document.id


def add_document(title, file_path, file_tag, user_id, upload_time, update_time):
    """添加文档"""
    new_document = Documents(title=title, file_path=file_path, file_tag=file_tag,
                             user_id=user_id, upload_time=upload_time,
                             update_time=update_time)

    return new_document.id


def update_document(document):
    """更新文档信息"""
    document_id = document["id"]
    old_document = select_document_by_id(document_id)
    old_document.title = document["title"]
    old_document.file_tag = document["file_tag"]
    old_document.update_time = document["update_time"]
    db.session.commit()
    new_document = select_document_by_id(document_id)
    logger.info(f"原数据: {old_document.file_tag}; 新数据: {new_document.file_tag}")
    return new_document


def select_document_by_id(document_id):
    """根据文档id获取文档"""
    document = Documents.query.filter_by(id=document_id).first()
    return document


def select_all_document():
    """获取文档表的所有数据"""
    return Documents.query.all()

def delete_document(document_id):
    """根据id删除文档"""
    document = Documents.query.filter_by(id=document_id)
    document.delete()  # 删除
    db.session.commit()
    return True
