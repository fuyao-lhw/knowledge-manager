"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/2/26 13:55
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  documentsMapper.py

功能描述

实现步骤

"""
import datetime
from flask import Blueprint, request, jsonify
from perKnowManage.config import logger
from perKnowManage.service.documentService import (
    get_document_list_service, get_document_detail, get_stats_service,
    upload_document_service
)

bp = Blueprint("documents", __name__)


# 文档上传方法
@bp.route("/documents", methods=["POST"])
def documents():
    if request.method == "POST":
        logger.info("上传文件接口")

        # 获取参数
        data = request.form  # 获取附带参数
        username = data.get("username")  # 获取发送者的用户名
        fileInfos = data.get("fileInfos")  # 文档信息
        fileList = request.files.getlist("files")  # 获取文件列表

        upload_document_service(username, fileInfos, fileList)


        # # file_content = file.read().decode("utf-8")  # 文件内容
        # # print(file_content)  # 读取文件内容
        # filename = file.filename  # 文件名
        # save_path = os.path.join(FILE_FOLDER, filename)  # 保存的路径
        # # file.save(save_path)
        # logger.info(f"发送者: {username}; 文件保存至: {save_path}")
        # logger.info(f"{file.filename}保存成功!")
        #
        # dtm = DocumentToMySQL()  # 创建对象
        #
        # # 入库-documents
        # logger.info(f"将文档数据写入documents表")
        # title = filename.title()  # 文档标题
        # file_path = save_path  # 文件路径
        # file_type = title.split('.')[-1]  # 文件类型
        # user_id = select_user_id_by_username(username)  # 上传用户
        # logger.info(f"标题:{title},路径:{file_path},类型:{file_type},用户:{user_id}")
        # # document_id = dtm.save_to_documents(title, file_path, file_type, user_id)  # 添加
        # logger.info("数据添加成功!")
        #
        # # 入表-tags
        # logger.info(f"将标签列表数据写入标签表")
        # tags = list(eval(tags if tags else filename.split(".")[-1]))  # 将字符串转为列表
        # logger.info(f"文件名: {filename}; 文档标签: {tags}; 类型: {type(tags)}")
        # # tags_id_list = dtm.save_to_tags(tags, user_id)  # 添加
        #
        # # 入表-documents_tags
        # logger.info(f"将文档id和标签id一一对应")
        # # dtm.save_to_documents_tags(document_id, tags_id_list)

        return jsonify({
            "status": 200,
            "message": "上传成功"
        })


# 获取文档列表
@bp.route("/documents", methods=["GET"])
def get_document_list():
    if request.method == "GET":
        logger.info("文档列表接口")
        data = request.args
        form = data["form"]
        logger.info(f"请求形式:{form}")
        return get_document_list_service(form)


# 更新文档
@bp.route("/documents/<document_id>", methods=["PUT"])
def update_documents(document_id):
    logger.info(f"文档更新接口: {document_id}")


# 获取文档详细内容
@bp.route("/documents/<document_id>", methods=["GET"])
def get_documents_details(document_id):
    if request.method == "GET":
        logger.info("获取文档的详细信息")
        return get_document_detail(document_id)


@bp.route("/stats", methods=["GET", "POST"])
def stats():
    if request.method == "GET":
        logger.info("读取数据展示信息")
        return get_stats_service()
