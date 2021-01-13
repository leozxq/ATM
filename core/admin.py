from core import src
from interface import bank_interface,admin_interface
def admin_run():
    def register():
        src.register()

    def change_balance():
        while True:
            login_user=src.login_user
            username=input('需要调整的账号：')
            newbalance=input('余额调整为：')
            flag,msg = admin_interface.change_balance_interface(login_user,username,newbalance)
            if flag:
                print(msg)
                break

    def lock():
        while True:
            login_user=src.login_user
            username=input('请输入需要冻结的账户：')
            flag,msg=admin_interface.lock_interface(login_user,username)
            if flag:
                print(msg)
                break
            else:
                print(msg)

    def add_product():
        while True:
            name=input('请输入商品名称：')
            price=input('请输入价格：')
            if not float(price):
                continue
            flag,msg=admin_interface.add_product_interface(name,float(price))
            if flag:
                print(msg)
                break
            print('添加商品失败')

    admin_dict={
        '1':register,
        '2':change_balance,
        '3':lock,
        '4':add_product
    }
    while True:
        print(
            '''
            1. 创建账户
            2. 修改余额
            3. 冻结账户
            4. 添加商品
            '''
        )
        choice=input('请输入功能编号：')
        admin_dict.get(choice)()
    return None