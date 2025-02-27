"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/2/27 19:51
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  send_email.py

功能描述

实现步骤

"""
import datetime

'''
encoding:   -*- coding: utf-8 -*-
@Time           :  2024/10/2 12:47
@Project_Name   :  Python
@Author         :  lhw
@File_Name      :  send_email.py

功能描述

实现步骤

'''
import lhw_send_email
import random
import time
from perKnowManage.config import logger

times = 0

code_ts = {}


def send(destination, form):
    global code_ts
    print('发送中...')
    print('目标邮箱:', destination)
    fromEmailAddress = '1959415641@qq.com'
    password = 'vrpphqonlthjbcea'
    subject = ''
    content = ''
    if form == 'code':
        subject = '扶摇知识管理系统注册'
        # 随机生成6位验证码
        codes = [str(random.randint(0, 9)) for i in range(6)]
        code = ''.join(codes)
        code_ts['code'], code_ts['ts'] = code, datetime.datetime.now()
        content = (f'欢迎来到扶摇知识管理系统!\n'
                   f'您的注册验证码为:\n'
                   f'{code}\n'
                   f'感谢您的注册!!!')
    elif form == 'register':
        subject = '扶摇论坛'
        content = ('欢迎来到扶摇知识管理系统!!!\n'
                   '恭喜您注册成功!!!\n'
                   '感谢您的使用!!!')
    s = lhw_send_email.SendEmail(fromEmailAddress=fromEmailAddress,
                                 password=password, content=content,
                                 destination=destination, subject=subject, api=None)
    s.send()
    print('发送完毕...')
    return True


def verify_send_ts(ts):
    global times
    if times == 0:
        times = ts
        return True
    else:
        if ts - times <= 120:
            return False
        else:
            times = ts
            return True
