"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/2/26 12:29
@Project_Name   :  PerKownManage
@Author         :  lhw
@File_Name      :  __init__.py.py

功能描述

实现步骤

"""
from flask import Flask
from perKnowManage.config import db
from flask_cors import CORS


# 创建应用
def create_app():
    # __name__是此模块(per..age)的名字,用以设置路径
    # instance...config: 告诉应用实例文件夹处于模块的外面
    app = Flask(__name__)
    app.config.from_object(__name__)
    # 设置最大文件上传大小为 10MB
    app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lhw050727@localhost/perknowmanage'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 配置是否追踪对象的修改（建议生产环境中设置为False以提高性能）
    # 绑定db
    db.init_app(app)
    # 跨域
    CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)

    url_prefix = "/api"

    # 登录注册功能
    from perKnowManage.controller import identityController
    app.register_blueprint(blueprint=identityController.bp, url_prefix=url_prefix)

    # 文档功能
    from perKnowManage.controller import documentsController
    app.register_blueprint(blueprint=documentsController.bp, url_prefix=url_prefix)

    # 标签
    from perKnowManage.controller import  tagsController
    app.register_blueprint(blueprint=tagsController.bp, url_prefix=url_prefix)

    return app
