from lib import common
from db import db_handler


def change_balance_interface(login_user, username, newbalance):
    user_dict = db_handler.check(username)
    user_dict['balance'] = float(newbalance)
    flow = f"{common.gettime()}: {username}的余额被{login_user}条整为{user_dict['balance']}."
    user_dict['flow'].append(flow)
    db_handler.save(user_dict)
    return True, flow


def lock_interface(login_user, username):
    user_dict = db_handler.check(username)
    if user_dict:
        choice = input('1. 冻结账户。/n2. 解锁账户。 /n请选择：')
        if choice == '1':
            user_dict['locked'] = True
            flow = f"{username}账户已冻结。"
            user_dict['flow'].append(flow)
        else:
            user_dict['locked'] = False
            flow = f"{username}账户已解冻。"
            user_dict['flow'].append(flow)
        db_handler.save(user_dict)
        return True, flow
    return False, f"用户不存在，请重新输入："


def add_product_interface(name, price):
    data = db_handler.check_product_list()
    data.append([name, price])
    db_handler.add_product_list(data)
    return True, f"已添加商品{name},单价{price}"
