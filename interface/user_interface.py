from db import db_handler
from lib import common
def register_interface(username,password,balance=15000):
    user_dict=db_handler.check(username)
    if user_dict:
        return False, "%s 用户已经存在，请重新输入用户名："%username
    else:
        password=common.get_pwd_md5(password)
        user_dict={
            "username":username,
            "password":password,
            'balance': balance,
            'flow': [],  # 用户流水
            'shop_car': {},
            'locked': False,  # 用户是否被冻结
        }
        db_handler.save(user_dict)
        return True, "%s 用户创建成功"%username

def login_interface(username,password):
    user_dict=db_handler.check(username)
    password=common.get_pwd_md5(password)
    if password==user_dict.get('password'):
        return True, "%s 登录成功。"%username
    return False, "%s 登录失败，密码不正确，请重新输入"%username

def check_balance_interface(username):
    user_dict=db_handler.check(username)
    return user_dict.get('balance')

