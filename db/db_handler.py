from conf import settings
import os,json


def save(data):
    username=data.get('username')
    userdata_file=os.path.join(settings.user_data_path,f'{username}.json')
    with open(userdata_file,'w',encoding='utf-8') as f:
        user_dict=json.dump(data,f,ensure_ascii=False)
        return user_dict

def check(username):
    userdata_file=os.path.join(settings.user_data_path,f'{username}.json')
    if os.path.isfile(userdata_file):
        with open(userdata_file,'r') as f:
            user_dict=json.load(f)
            return user_dict
    return None

