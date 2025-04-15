"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/2/27 19:03
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  identityController.py

功能描述

实现步骤

"""
from flask import Blueprint, request, jsonify
from perKnowManage.config import logger, db
from perKnowManage.pojo.models import Users
import datetime
import time
from perKnowManage.service.identityService import (
    login_service, register_service, login_state_service, trans_pwd_service,
    verify_code_service
    )

bp = Blueprint("identity", __name__)


@bp.route("/login", methods=["POST"])
def login_controller():
    logger.info(f"用户登录")
    if request.method == "POST":
        data = request.get_json()
        logger.info(data)
        # 获取邮箱和密码
        email, password = data["email"], data["password"]
        return login_service(email, password)


@bp.route("/register", methods=["POST"])
def register_controller():
    logger.info(f"用户注册")
    if request.method == "POST":
        data = request.get_json()
        logger.info(data)
        # 结构
        email, password, code = data["email"], data["password"], data["code"]
        return register_service(email, password, code)


@bp.route('/login/verify', methods=['POST', 'GET'])
def verify_login_ts_controller():
    logger.info("校验登录状态")
    if request.method == 'POST':
        data = request.get_json()
        logger.info(data)
        # 解构
        email, ts = data['username'], datetime.datetime.now()
        return login_state_service(email, ts)


@bp.route('/verify_code', methods=["POST", "GET"])
def verify_code_controller():
    print("发送验证码")
    if request.method == "POST":
        data = request.get_json()
        destination = data['email']
        return verify_code_service(destination)


@bp.route("/trans_pwd", methods=["GET", "POST"])
def trans_password_controller():
    """修改密码的验证"""
    if request.method == "POST":
        data = request.get_json()
        email, old_pwd, new_pwd, confirm_pwd, verify_code = data["email"], data["old_pwd"], data["new_pwd"], data[
            "confirm_pwd"], data["verify_code"]
        return trans_pwd_service(verify_code, email, new_pwd)