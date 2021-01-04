import hashlib


def get_pwd_md5(password):
    md5_obj=hashlib.md5()
    md5_obj.update(password.encode(encoding='utf-8'))
    salt=f'动态'
    md5_obj.update(salt.encode(encoding='utf-8'))
    return md5_obj.hexdigest()

def login_auth(func):
    from core import src

    def inner(*args,**kwargs):
        if src.login_user:
            res=func(*args,**kwargs)
            return res
        else:
            print('用户未登录')
            src.login()
            res=func(*args,**kwargs)
            return res
    return inner