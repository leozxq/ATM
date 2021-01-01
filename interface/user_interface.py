from db import db_handler

def register_interface(username,password,balance=15000):
    user_dict=db_handler.check(username)
    if user_dict:
        return False, "%s 用户已经存在，请重新输入用户名："%username
    else:
        user_dict={
            "username":username,
            "password":password,
            'blance': balance,
            'flow': [],  # 用户流水
            'shop_car': {},
            'locked': False,  # 用户是否被冻结
        }
        user_dict=db_handler.save(user_dict)
        return True, "%s 用户创建成功"%username
