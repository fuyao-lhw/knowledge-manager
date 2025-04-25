"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/21 16:10
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  getEntityRelationship.py

功能描述
    使用nltk库,对文档内容进行知识关联
实现步骤

"""
import requests
from perKnowManage.mapper.tagsMapper import get_all_tags
from perKnowManage import create_app
from perKnowManage.pojo.models import Documents, Tags, document_tags
from perKnowManage.config import db


def get_example_data():
    url = "https://echarts.apache.org/examples/data/asset/data/les-miserables.json"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0"
    }
    response = requests.get(url=url, headers=headers)
    result = response.json()

    print(result)
    return result


def find_related_documents():
    """查找具有共同标签的文档对"""
    # with app.app_context():
    # 为表创建别名
    dt1 = document_tags.alias()
    dt2 = document_tags.alias()
    doc1_table = Documents.__table__
    doc2_table = doc1_table.alias()

    # 执行查询
    results = db.session.query(
        doc1_table.c.id.label('doc1_id'),
        doc1_table.c.title.label('doc1_title'),
        doc2_table.c.id.label('doc2_id'),
        doc2_table.c.title.label('doc2_title'),
        Tags.name
    ).join(
        dt1, doc1_table.c.id == dt1.c.document_id
    ).join(
        Tags, dt1.c.tag_id == Tags.id
    ).join(
        dt2, Tags.id == dt2.c.tag_id
    ).join(
        doc2_table, dt2.c.document_id == doc2_table.c.id
    ).filter(
        doc1_table.c.id < doc2_table.c.id
    ).order_by(
        Tags.name
    ).all()


    tags = get_all_tags()
    categories = [
        {"name": t} for t in tags
    ]
    print(f"categories: {categories}")

    links = []

    # 输出结果
    for result in results:



        print(f"文档1 ID: {result.doc1_id}, 文档1标题: {result.doc1_title}, "
              f"文档2 ID: {result.doc2_id}, 文档2标题: {result.doc2_title}, "
              f"共同标签: {result.name}")




def generate_echarts_data():
    # with app.app_context():
    all_documents = Documents.query.all()
    all_tags = Tags.query.all()

    nodes = []
    links = []

    # 生成节点数据
    for doc in all_documents:
        nodes.append({
            'name': doc.title,
            'category': 'document'
        })
    for tag in all_tags:
        nodes.append({
            'name': tag.name,
            'category': 'tag'
        })

    # 生成边数据
    for doc in all_documents:
        for tag in doc.file_tag:
            links.append({
                'source': doc.title,
                'target': tag
            })
    result = {
        'nodes': nodes,
        'links': links
    }

    print(result)

    return result


def run():
    app = create_app()
    with app.app_context():
        # get_example_data()
        tags = get_all_tags()
        print([tag.name for tag in tags])
        find_related_documents()
        # generate_echarts_data()


if __name__ == '__main__':
    run()
