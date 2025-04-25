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
from perKnowManage.mapper.tagsMapper import (
    select_tag_id_by_tag, add_tag, select_tag_by_id)
from perKnowManage.service.documents_tagsService import add_did_tid_service
from perKnowManage.pojo.models import document_tags
from perKnowManage.mapper.documents_tagsMapper import delete_by_did_tid


def sync():
    documents = select_all_document()
    for d in documents:  # 遍历文档
        tags = [d.file_tag] if len(d.file_tag) == 1 else d.file_tag.split(',')
        print(d.id, tags)
        delete_surplus_dt(did=d.id, dtags=tags)
        for tag in tags:  # 遍历标签
            global tag_id
            try:
                tag_id = select_tag_id_by_tag(tag)
            except AttributeError:
                print(f"添加标签: {tag}")
                add_tag(tag_name=tag, user_id=3)
            print(tag, tag_id, d.id)
            add_did_tid_service(d.id, tag_id)


def delete_surplus_dt(did, dtags):
    """更新文档的标签时,删除多余的标签对应关系"""
    # dttags - document_tags表的标签; dtags - document表的标签
    dttag_list = db.session.query(document_tags).filter_by(document_id=did).all()
    dttags = [select_tag_by_id(d.tag_id) for d in dttag_list]
    # print(f"dttags: {dttags}; dtags: {dtags}")
    dttags = set(dttags)
    dtags = set(dtags)
    print(f"dttags: {dttags}; dtags: {dtags}")
    diff = list(dttags - dtags)  # 差集
    print(f"差集: {diff}")
    for d in diff:
        tag_id = select_tag_id_by_tag(d)
        delete_by_did_tid(did, tag_id)


def standalone_run():
    from perKnowManage import create_app  # 延迟导入防止循环依赖
    app = create_app()
    with app.app_context():
        sync()


if __name__ == '__main__':
    standalone_run()
