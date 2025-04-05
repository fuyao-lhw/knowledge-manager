"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/2/26 12:50
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  app.py

功能描述

实现步骤

"""
from perKnowManage import create_app


if __name__ == '__main__':
    app = create_app()
    # with app.app_context():
    #     run_content_to_db()
    app.run(debug=True)
