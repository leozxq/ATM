from conf import settings
import os,json

def save(data):
    username=data.get('username')
    userdata_file=os.path.join(settings.user_data_path,f'{username}.json')
    with open(userdata_file,'w',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False)

def check(username):
    userdata_file=os.path.join(settings.user_data_path,f'{username}.json')
    if os.path.isfile(userdata_file):
        with open(userdata_file,'r',encoding='utf-8') as f:
            user_dict=json.load(f)
            return user_dict
#读取商品字典
def check_product_list():
    shop_list_file = os.path.join(settings.shop_data_path, 'shop_list.json')
    with open(shop_list_file,'r',encoding='utf-8') as f:
        shop_list =json.load(f)
        return shop_list
# 保存商品字典
def add_product_list(data):
    shop_list_file=os.path.join(settings.shop_data_path,'shop_list.json')
    with open(shop_list_file,'w',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False)


