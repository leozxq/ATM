from db import db_handler
from lib import common
import logging.config
from conf import settings
logging.config.dictConfig(settings.LOGGING_DICT)
ATM_logger=logging.getLogger('ATM')

def withdraw_interface(login_user,money):
    #手续费5%
    money2=float(money)*1.05
    user_dict=db_handler.check(login_user)
    balance=user_dict["balance"]
    if float(balance)>=money2:
        user_dict["balance"]-=money2
        flow=f"{common.gettime()}: {login_user} 提现成功，提现金额为{money},余额为{user_dict.get('balance')}, 本次手续费为{money2-float(money)}"
        user_dict['flow'].append(flow)
        ATM_logger.info(flow)
        db_handler.save(user_dict)
        return True, flow
    flow=f"{login_user} 提现失败，余额不足，余额为{user_dict.get('balance')}，请重新输入提现金额。"
    ATM_logger.warning(flow)
    return False, flow

def repay_interface(login_user,money):
    user_dict=db_handler.check(login_user)
    user_dict['balance']+=money
    flow=f"{common.gettime()}: {login_user} 还款成功，还款金额{money},账户余额{user_dict['balance']}."
    user_dict['flow'].append(flow)
    ATM_logger.info(flow)
    db_handler.save(user_dict)
    return True, flow


def transfer_interface(login_user,to_user, money):
    to_user_dict=db_handler.check(to_user)
    if to_user_dict:
        login_user_dict=db_handler.check(login_user)
        if login_user_dict['balance']>=money:
            login_user_dict['balance']-=money
            to_user_dict['balance']+=money
            login_user_flow=f"{common.gettime()}: 转账成功，{login_user}给{to_user} 转账，金额为{money},账户余额为{login_user_dict['balance']}."
            login_user_dict['flow'].append(login_user_flow)
            to_user_flow=f"{common.gettime()}: 转账成功，{to_user}收到{login_user} 转账，金额为{money},账户余额为{to_user_dict['balance']}."
            to_user_dict['flow'].append(to_user_flow)
            ATM_logger.info(login_user_flow)
            db_handler.save(login_user_dict)
            db_handler.save(to_user_dict)
            return True, login_user_flow
        else:
            flow=f"转账失败，余额不足。,账户余额为{login_user_dict['balance']}."
            ATM_logger.info(flow)
            return False, flow
    else:
        return False,f"{login_user}{to_user}不存在，请重新输入。"


def check_flow_interface(login_user):
    user_dict=db_handler.check(login_user)
    flow_list=user_dict['flow']
    return flow_list