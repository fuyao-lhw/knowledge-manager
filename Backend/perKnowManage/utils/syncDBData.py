"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/19 12:49
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  syncDBData.py

功能描述
    同步数据库数据 -document_tags表
实现步骤
    1.读取documents表-获取文档id与其对应的标签
    2.根据标签获取对应的标签id
    3.查询文档id是否与这些标签id对应,对应了跳过,否则新增
"""
from perKnowManage.config import db
from perKnowManage.mapper.documentsMapper import select_all_document
from perKnowManage.mapper.tagsMapper import select_tag_id_by_tag
from perKnowManage.service.documents_tagsService import add_did_tid_service


def sync():
    documents = select_all_document()
    for d in documents:  # 遍历文档
        tags = [d.file_tag] if len(d.file_tag) == 1 else d.file_tag.split(',')
        for tag in tags:  # 遍历标签
            tag_id = select_tag_id_by_tag(tag)
            print(tag, tag_id, d.id)
            add_did_tid_service(d.id, tag_id)


def standalone_run():
    from perKnowManage import create_app  # 延迟导入防止循环依赖
    app = create_app()
    with app.app_context():
        sync()


if __name__ == '__main__':
    standalone_run()