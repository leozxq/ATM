import os

BASH_PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

user_data_path=os.path.join(BASH_PATH,'db','user_data')
shop_data_path=os.path.join(BASH_PATH,'db','shop_data')
logs_file_path=os.path.join(BASH_PATH,'db','logs','logs.log')

#定义日志字典
#1. 日志输出格式
full_format='[%(asctime)s] [%(threadName)s:%(thread)d] [%(process)d ]\
 [%(filename)s:%(lineno)d] [%(levelname)s] [%(message)s]'
simple_format='[%(asctime)s] [%(levelname)s]\
 [%(filename)s:%(lineno)d] [%(message)s]'
#2. 日志字典
LOGGING_DICT={
    'version':1,
    'disable_existing_loggers':True,
    'formatters':{
        'full':{
            'format':full_format,
            'datefmt':'%Y-%m-%d %H:%M:%S',
        },
        'simple':{
            'format':simple_format,
            'datefmt':'%Y-%m-%d %H:%M:%S',
        }
    },
    'filters':{},
    #日志处理器，接受日志，输出到指定位置
    'handlers':{
        #将日志输出到文件
        'file':{
            'level':'DEBUG',    #第二层日志级别过滤
            'class':'logging.FileHandler',
            'formatter':'full',
            'filename': logs_file_path,
            'encoding':'utf-8',
        },
        #将日志输出到终端
        'console':{
            'level':'WARNING',
            'class':'logging.StreamHandler',
            'formatter':'simple',
        },
    },
    #日志记录器，产生日志，传给日志处理器
    'loggers':{
        'ATM':{
            'handlers':['console','file'],
            'level':'DEBUG', #第一层日志级别过滤
            'propagate':False,
        }
    },
}