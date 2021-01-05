from interface import user_interface, bank_interface, shop_interface
from lib import common

login_user = None


def register():
    while True:
        username = input('请输入用户名：')
        password = input('请输入密码：')
        repassword = input('请再次输入密码：')
        if password == repassword:
            flag, msg = user_interface.register_interface(username, password)
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
        username = input("请输入用户名：")
        password = input("请输入密码：")
        flag, msg = user_interface.login_interface(username, password)
        if flag:
            print(msg)
            global login_user
            login_user = username
            break
        print(msg)


@common.login_auth
def check_balance():
    username = login_user
    balance = user_interface.check_balance_interface(username)
    print(f"{username} 用户的余额为{balance}")


@common.login_auth
def withdraw():
    while True:
        money = input("请输入提现金额：")
        if not money.isdigit():
            print('请输入正确金额：')
            continue
        flag, msg = bank_interface.withdraw_interface(login_user, money)
        if flag:
            print(msg)
            break
        print(msg)

@common.login_auth
def repay():
    while True:
        input_money=input('请输入还款金额：')
        try:
            input_money=float(input_money)
        except ValueError:
            print('请输入正确金额：')
            continue
        if input_money >0:
            flag,msg=bank_interface.repay_interface(login_user,input_money)
            if flag:
                print(msg)
                break
        else:
            print('输入金额不能小于0。')

@common.login_auth
def transfer():
    while True:
        to_user=input('请输入对方账号：')
        money=input('请输入转账金额：')
        try:
            money=float(money)
        except ValueError:
            print('请输入正确金额：')
            continue
        if money >0:
            flag,msg=bank_interface.transfer_interface(login_user,to_user,money)
            if flag:
                print(msg)
                break
            else:
                print(msg)
        else:
            print('输入金额不能小于0。')


@common.login_auth
def check_flow():
    flow_list=bank_interface.check_flow_interface(login_user)
    if flow_list:
        for flow in flow_list:
            print(flow)
    else:
        print(f'{login_user}没有流水！')

@common.login_auth
def shopping():
    pass

@common.login_auth
def check_shop_car():
    pass

@common.login_auth
def admin():
    from core import admin
    admin.admin_run()
    pass


# 创建函数功能字典
func_dict = {
    '1': register,
    '2': login,
    '3': check_balance,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shopping,
    '9': check_shop_car,
    '10': admin,
}


# 视图层主函数
def run():
    while True:
        print('''
                =====用户界面=====
                1. 注册功能
                2. 登录功能
                3. 查看余额
                4. 提现
                5. 还款
                6. 转账
                7. 查看流水
                8。 购物功能
                9. 查看购物车
                10. 管理员功能
                =====感谢使用=====
                ''')

        chioce = input('请输入功能编号：')
        func_dict.get(chioce)()
