"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/2/27 19:03
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  identity.py

功能描述

实现步骤

"""
from flask import Blueprint, request, jsonify
from perKnowManage.config import logger, verify_code_temp, db
from perKnowManage.Models.models import Users
import datetime
import time
from perKnowManage.utils.sendEmail import verify_send_ts, send, code_ts

bp = Blueprint("identity", __name__)


@bp.route("/login", methods=["POST"])
def login():
    logger.info(f"api: /login")
    if request.method == "POST":
        data = request.get_json()
        print(data)
        # 结构
        email, password = data["email"], data["password"]
        # 时间
        ts = int(time.time())
        logger.info(f"api: /login;  user: {email}")
        user = Users.query.filter_by(email=email).first()
        if user is None:
            return jsonify({
                "status": 100,
                "message": "用户未注册",
                "data": "",
            })
        else:
            if user.password == password:
                # 更新时间
                user.login_ts = datetime.datetime.now()
                db.session.commit()
                return jsonify({
                    "status": 200,
                    "message": f"用户{email}登录成功,登录时间:{ts}"
                })
            else:
                return jsonify({
                    "status": 100,
                    "message": "用户密码不正确"
                })


@bp.route("/register", methods=["POST"])
def register():
    logger.info(f"api: /register")
    if request.method == "POST":
        data = request.get_json()
        print(data)
        # 结构
        email, password, code = data["email"], data["password"], data["code"]
        logger.info(f"api: /register;  user:{email}")
        ts = datetime.datetime.now()
        print(code_ts, code, (ts - code_ts['ts']).total_seconds())
        if code == code_ts["code"] and (ts - code_ts['ts']).total_seconds() <= 120:
            try:
                # 添加数据
                new_user = Users(email=email, password=password, created_at=ts, login_ts=ts)
                db.session.add(new_user)
                db.session.commit()
                send(destination=email, form='register')
                logger.info(f"{email}注册成功!, 时间为{ts}")
                return jsonify({
                    'status': 200,
                    'message': f'注册成功!注册时间:{ts}',

                })
            except Exception as e:
                print(f'发生报错:\n{e}')
                return jsonify({
                    'status': 100,
                    'message': '注册失败!请联系网站管理员哟~~~',
                })
        else:
            return jsonify({
                'status': 100,
                'message': '验证码失效或者错误',
            })


@bp.route('/login/verify', methods=['POST', 'GET'])
def verify_login_ts():
    if request.method == 'POST':
        data = request.get_json()
        logger.info(f'api:/verify_ts 接收到数据:\n{data}')
        # 解构
        email, ts = data['username'], datetime.datetime.now()
        # 查询
        user = Users.query.filter_by(email=email).first()
        ts, user.ts = datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M:%S'), datetime.datetime.strptime(user.ts,
                                                                                                      '%Y-%m-%d %H:%M:%S')
        # logger.info(ts, user.ts, ts - user.ts)
        if ts - user.ts < datetime.timedelta(days=7):
            return jsonify({
                'status': 200,
                'message': f'时间验证成功,上一次登录时间:{ts}',
            })
        return jsonify({
            'status': 100,
            'message': '时间验证失败!请重新登录',
        })


@bp.route('/verify_code', methods=["POST", "GET"])
def verify_code():
    # # 创建用户时传入 datetime 对象
    # new_user = Users(
    #     email="2704316524@qq.com",
    #     password="lhw050727",
    #     created_at=datetime.datetime.now(),  # 直接传入 datetime 对象
    #     login_ts=datetime.datetime.now()
    # )
    # db.session.add(new_user)
    # db.session.commit()
    print('接口:/verify_code')
    if request.method == "POST":
        data = request.get_json()
        destination = data['email']
        ts = int(time.time())
        if verify_send_ts(ts):
            if send(destination=destination, form='code'):
                return jsonify({
                    'status': 200,
                    'message': '发送成功',
                    'data': {"ts": ts},
                })
            else:
                return jsonify({
                    'status': 100,
                    'message': '发送失败',
                    'data': {"ts": ts},
                })
            # return jsonify({
            #     'msg': '时间已过2min,原验证码已失效,已经再次发送',
            #     'isCorrect': False,
            # })
        else:
            return jsonify({
                'message': '时间未过2min,原验证码未失效',
                'status': 200,
            })


@bp.route("/trans_pwd", methods=["GET", "POST"])
def trans_password():
    """修改密码的验证"""
    if request.method == "POST":
        data = request.get_json()
        email, old_pwd, new_pwd, confirm_pwd, verify_code = data["email"], data["old_pwd"], data["new_pwd"], data[
            "confirm_pwd"], data["verify_code"]
        ts = datetime.datetime.now()
        if verify_code == code_ts["code"] and (ts - code_ts["ts"]).total_seconds() <= 120:
            user = Users.query(email=email)
            if user.password == new_pwd:
                return jsonify({
                    "status": 100,
                    "message": "新密码不能与旧密码一样"
                })
            else:
                user.password = new_pwd
                db.session.commit()
                return jsonify({
                    "status": 200,
                    "message": f"密码修改成功!时间:{datetime.datetime.now()}"
                })
        else:
            return jsonify({
                "status": 100,
                "message": "验证码失效或错误",
            })
