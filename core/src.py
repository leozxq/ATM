
from interface import user_interface

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
