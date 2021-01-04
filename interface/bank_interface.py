from db import db_handler

def withdraw_interface(login_user,money):
    #手续费5%
    money2=float(money)*1.05
    user_dict=db_handler.check(login_user)
    balance=user_dict["balance"]
    if float(balance)>=money2:
        user_dict["balance"]-=money2
        a=db_handler.save(user_dict)
        return True, f"{login_user} 提现成功，提现金额为{money},余额为{user_dict.get('balance')}, 本次手续费为{money2-float(money)}"
    return False, f"{login_user} 提现失败，余额不足，余额为{user_dict.get('balance')}，请重新输入提现金额。"

