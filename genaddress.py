from random import *
import json
from weight_choice import *
from genpassword import *
from pyexcel import *
from classifyaddress import *

#type 1
title_pattern = ['我', '我的', '']
pronounce = ['现', '现在', '']
feature = ['住址', '住的', '地址', '居住地址', '房子地址', '身份证地址', '']
tense = ['是', '在', '']
feature_tail = ['那个', '']
position = ['', '旁边','边上','对面','后面','隔壁','这边','东边','西边','南边','北边']
Modal = [ '', '啊','额','嗯', '唉', '哦']

#type 2
head_p = ['我',choice(Modal),'']
conjunction = ['那个', '就','就知道', '']
tense1 = ['是', '在','是在','']
verb = ['','住']

#TYPE3
title_pattern1 = ['我',  '']
pronounce1 = ['现在', '']
verb1 = ['住', '在','住在','']
feature_tail1 = ['那个', '这个', '']

def address_type1():
    label_status, address = get_address()
    address_raw1 =  Modal[windex([3,2, 2, 2,1,1])]+choice(title_pattern) +pronounce[windex([3,2,3])]+feature[windex([2,2,2,1,1,1,2])]  +tense[windex([1,1,1])]\
                   +feature_tail[windex([1,3])]+address + position[windex([5,2,2,2,1,1,1,1,1,1,1])]
    return address_raw1, address, label_status

def address_type2():
    label_status, address = get_address()
    address_raw2 = head_p[windex([1,1,3])]+ choice(conjunction) + choice(tense1)+ address + position[windex([5,2,2,2,1,1,1,1,1,1,1])]+verb[windex([5,1])]
    return address_raw2, address,label_status

def address_type3():
    label_status, address = get_address()
    address_raw3 = choice(title_pattern1) + choice(pronounce1) +choice(verb1) + choice(feature_tail1)+address+position[windex([5,2,2,2,1,1,1,1,1,1,1])]
    return address_raw3, address, label_status

def gen_address():
    address_list =[ address_type2(), address_type1(),address_type3()]
    address_ref, address_write, address_status = address_list[windex([5,3,1])]
    return address_ref, address_write, address_status

if __name__ == "__main__":
    num_data = 2
    list_data = list()
    label_name = 'address'
    for i in range(num_data):
        list_dict = dict()
        list_dict['label_name'] = label_name
        list_dict['id'] = i
        list_dict['ref'], list_dict['write'],address_status = gen_address()
        list_dict['province'] = address_status['province']
        list_dict['city'] = address_status['city']
        list_dict['county'] = address_status['county']
        print(list_dict)
            #     list_data.append(list_dict)
    #     print('loading')
    # obj = json.dumps(list_data, ensure_ascii=False, indent=2)
    # file = open('/home/yzs/'+label_name+'_gen_0425_'+str(num_data)+'.json', 'w')
    # file.write(obj)
    # file.close()
