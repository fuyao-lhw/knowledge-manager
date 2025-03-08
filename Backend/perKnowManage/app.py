"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/2/26 12:50
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  app.py

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

    # 配置数据库
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lhw050727@localhost/perknowmanage'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 配置是否追踪对象的修改（建议生产环境中设置为False以提高性能）
    # 绑定db
    db.init_app(app)
    # 跨域
    CORS(app, resources={r'/*': {'origins': '*'}}, supports_credentials=True)

    url_prefix = "/api"

    # 登录注册功能
    from perKnowManage.Apis import identity
    app.register_blueprint(blueprint=identity.bp, url_prefix=url_prefix)

    # 文档功能
    from perKnowManage.Apis import documents
    app.register_blueprint(blueprint=documents.bp, url_prefix=url_prefix)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
