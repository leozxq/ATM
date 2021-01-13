import hashlib,time
from conf import settings


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

def gettime():
    nowtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return nowtime

# import logging

# '''
# name='宝宝'
# #logging.basicConfig(level=logging.DEBUG,filename='log1.log',filemode='w')
# logging.basicConfig(level=logging.DEBUG)
# logging.debug(f"debug,{name}")
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
# '''
#日志级别，以最严格为准
#记录器
# logger=logging.getLogger('myATM')
# logger.setLevel(logging.DEBUG)
# #处理器
# consolehandler=logging.StreamHandler()
# consolehandler.setLevel(logging.DEBUG)
# filehandler=logging.FileHandler(filename=settings.logs_file_path)
# filehandler.setLevel(logging.WARNING)
# #格式
# formater=logging.Formatter("%(asctime)s|%(levelname)-8s|%(filename)10s:%(lineno)10s|%(message)s")
# #给处理器设置格式
# consolehandler.setFormatter(formater)
# filehandler.setFormatter(formater)
# #给记录器分配处理器
# logger.addHandler(consolehandler)
# logger.addHandler(filehandler)
# #过滤器
# flt=logging.Filter('myATM')
# #给记录器分配过滤器
# logger.addFilter(flt)
#
# logger.debug("debug is coming")
# logger.info('info is coming')
# logger.warning('warning is coming')
# logger.error('error is coming')
# logger.critical('critical is coming')