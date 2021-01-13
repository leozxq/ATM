from db import db_handler
from lib import common
from conf import settings

import logging.config

logging.config.dictConfig(settings.LOGGING_DICT)
ATM_logger=logging.getLogger('ATM')

def register_interface(username, password, balance=15000):
    user_dict = db_handler.check(username)
    if user_dict:
        msg=f"{username} 用户已经存在，请重新输入用户名："
        ATM_logger.error(msg)
        return False, msg
    else:
        password = common.get_pwd_md5(password)
        user_dict = {
            "username": username,
            "password": password,
            'balance': balance,
            'flow': [],  # 用户流水
            'shop_car': {},
            'locked': False,  # 用户是否被冻结
        }
        msg=f"{username} 用户创建成功"
        db_handler.save(user_dict)
        # ATM_logger.info(msg)
        return True, msg


# 登录接口
def login_interface(username, password):
    user_dict = db_handler.check(username)
    if user_dict:
        if user_dict['locked']:
            return False, f"{username}账户已冻结，无法登录"
        password = common.get_pwd_md5(password)
        if password == user_dict.get('password'):
            msg=f"{username} 登录成功。"
            ATM_logger.info(msg)
            return True, msg
        msg=f"{username} 登录失败，密码不正确，请重新输入"
        ATM_logger.error(msg)
        return False, msg
    msg = f"账户{username}不存在。"
    # ATM_logger.error(msg)
    return False, msg


def check_balance_interface(username):
    user_dict = db_handler.check(username)
    return user_dict.get('balance')
