"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/4/15 22:19
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  identityService.py

功能描述

实现步骤

"""
from perKnowManage.pojo.models import Users
from flask import jsonify
import datetime
import time
from perKnowManage.config import db, logger
from perKnowManage.pojo.result import Result
from perKnowManage.utils.sendEmail import verify_send_ts, send, code_ts
from perKnowManage.mapper.identityMapper import get_user, add_user


def login_service(email, password):
    """登录服务"""
    user = get_user(email)
    ts = datetime.datetime.now()  # 当前时间
    if user is None:
        return Result(msg="用户未注册").success()
    else:
        if user.password == password:
            # 更新时间
            user.login_ts = datetime.datetime.now()
            db.session.commit()
            return Result(msg=f"用户{email}登录成功,登录时间:{ts}").success()
        else:
            return Result(msg="用户密码不正确").success()


def register_service(email, password, code):
    """注册服务"""
    ts = int(time.time())  # 当前时间
    logger.info(code_ts, code, (ts - code_ts['ts']).total_seconds())
    if code == code_ts["code"] and (ts - code_ts['ts']).total_seconds() <= 120:
        try:
            add_user(email, password)
            send(destination=email, form='register')
            logger.info(f"{email}注册成功!, 时间为{ts}")
            return Result(msg=f'注册成功!注册时间:{ts}').success()
        except Exception as e:
            logger.error(e)
            return Result(msg='注册失败!请联系网站管理员哟~~~').fail()
    else:
        return Result(msg='验证码失效或者错误').fail()


def login_state_service(email, ts):
    """校验登录状态服务"""
    # 查询
    user = get_user(email)
    ts, user.ts = datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M:%S'), datetime.datetime.strptime(user.ts,
                                                         '%Y-%m-%d %H:%M:%S')
    # logger.info(ts, user.ts, ts - user.ts)
    if ts - user.ts < datetime.timedelta(days=7):
        return Result(msg=f'时间验证成功,上一次登录时间:{ts}').success()
    return Result(msg='时间验证失败!请重新登录').fail()


def verify_code_service(destination):
    """验证码服务"""
    ts = int(time.time())
    if verify_send_ts(ts):
        if send(destination=destination, form='code'):
            return Result(msg="发送成功", data={"ts": ts}).success()
        else:
            return Result(msg="发送失败", data={"ts": ts})
    else:
        return Result(msg='时间未过2min,原验证码未失效').fail()


def trans_pwd_service(verify_code, email, new_pwd):
    """修改密码服务"""
    ts = datetime.datetime.now()
    if verify_code == code_ts["code"] and (ts - code_ts["ts"]).total_seconds() <= 120:
        user = get_user(email)
        if user.password == new_pwd:
            return Result(msg="新密码不能与旧密码一样").fail()
        else:
            user.password = new_pwd
            db.session.commit()
            return Result(msg=f"密码修改成功!时间:{datetime.datetime.now()}").success()
    else:
        return Result(msg="验证码失效或错误").fail()
