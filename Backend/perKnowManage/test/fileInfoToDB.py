"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/3/31 14:48
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  fileInfoToDB.py

功能描述

实现步骤

"""
from perKnowManage.config import db
from perKnowManage.Models.models import Documents
from perKnowManage.test.getFileContent import *
import markdown
from datetime import datetime



file_list = get_file_list()
print(file_list)


def content_to_db(title, file_path, file_type, user_id, upload_time):
    new_documents = Documents(title=title, file_path=file_path,
                              file_type=file_type, user_id=user_id, upload_time=upload_time)

    db.session.add(new_documents)
    db.session.commit()
    print(f"{file_path} 添加成功")


def run_content_to_db():
    for file in file_list:
        file_path = os.path.join(FILE_FOLDER, file)
        # print(title)
        md_content = get_file_content(file_path)  # 读取内容
        # html = markdown.markdown(md_content)  # md转html
        content_to_db(file, file_path, "html", 3, datetime.now())


# 在 fileInfoToDB.py 底部添加
def standalone_run():
    from perKnowManage import create_app # 延迟导入防止循环依赖
    app = create_app()
    with app.app_context():
        run_content_to_db()

if __name__ == '__main__':
    standalone_run()
