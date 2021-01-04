
from interface import user_interface,bank_interface,shop_interface
from lib import common

login_user=None
def register():
    while True:
        username=input('请输入用户名：')
        password=input('请输入密码：')
        repassword=input('请再次输入密码：')
        if password==repassword:
            flag,msg=user_interface.register_interface(username,password)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('密码不一致，请重新输入')
            continue

def login():
    while True:
        username=input("请输入用户名：")
        password=input("请输入密码：")
        flag,msg=user_interface.login_interface(username,password)
        if flag:
            print(msg)
            global login_user
            login_user=username
            break
        print(msg)
@common.login_auth
def check_balance():
    username=login_user
    balance=user_interface.check_balance_interface(username)
    print(f"{username} 用户的余额为{balance}")

@common.login_auth
def withdraw():
    while True:
        money=input("请输入提现金额：")
        flag,msg= bank_interface.withdraw_interface(login_user,money)
        if flag:
            print(msg)
            break
        print(msg)
