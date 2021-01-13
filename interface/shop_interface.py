from db import db_handler
from lib import common
from conf import settings
import logging.config

logging.config.dictConfig(settings.LOGGING_DICT)
ATM_logger=logging.getLogger('ATM')

def get_product_list_interface():
    return db_handler.check_product_list()


def save_product_list_interface(name,price):
    shop_list=db_handler.check_product_list()
    shop_list.append([name,price])
    db_handler.add_product_list(shop_list)


def add_shop_car_interface(login_user, name, price):
    user_dict=db_handler.check(login_user)
    shop_car=user_dict['shop_car']
    if name in shop_car:
        shop_car[name][1]+=1

    else:
        add_product={name:[price,1]}
        shop_car.update(add_product)
    user_dict['shop_car']=shop_car
    flow=f"{common.gettime()}: 商品[{name}]已加入购物车。"

    ATM_logger.info(flow)
    db_handler.save(user_dict)
    return True,flow


def pay_shop_car_interface(login_user):
    cost=0
    user_dict=db_handler.check(login_user)
    if user_dict['shop_car']:
        for product in user_dict['shop_car'].values():
            print(product)
            cost+=int(product[0])*int(product[1])
        if user_dict['balance']>=cost:
            user_dict['balance']-=cost
            user_dict['shop_car']={}
            flow=f"{common.gettime()}: [{login_user}]已支付金额[{cost}]"
            db_handler.save(user_dict)
            ATM_logger.info(flow)
            return True, flow
        return False,f"余额不足，无法支付。"
    else:
        return False, f"未购买任何商品。"


def check_shop_car_interface(login_user):
    user_dict=db_handler.check(login_user)
    shop_car=user_dict['shop_car']
    if not shop_car:
        msg=f"账户[{login_user}]未添加购物车。"
        ATM_logger.info(msg)
        return False,msg
    return True, shop_car