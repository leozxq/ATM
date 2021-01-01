
import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


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
        select=input("请输入1-10，选择你想要的功能：")
        if select=='1':
            from core import src
            src.register()
        break

if __name__=="__main__":
    run()