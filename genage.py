from random import *
import json
from weight_choice import *
from genpassword import *
from genbirth import *
from listtojson import *

#type 1
title_pattern = ['我', '']
pronounce = ['今年', '现在', '']
tense = ['已经', '已', '']
feature = ['周岁', '虚岁', '']
feature_tail = ['岁', '']
Modal = ['啦', '']

#type 2
tense1 = ['不到', '']

#TYPE3
title_pattern1 = ['我', '我是', '']
# year_pattern = list()
born_pattern = ['出生', '生', '']
attribute = ['的', '']

#type4
pronounce1 = ['今年', '今年过了生日', '今年过去', '最近过了生日', '过了生日', '过段时间', '']
tense2 = ['就', '']

def age_type1():
    age = str(genageCN(18, 65))#或者调用n2c的full_n2c()函数
    age_raw1 = choice(title_pattern) +pronounce[windex([3,1,6])] +tense[windex([3,1,5])]+feature[windex([1,1,8])] +age + choice(feature_tail) + Modal[windex([2,8])]
    return age_raw1, age

def age_type2():
    age = str(genageCN(18, 65))
    age_raw2 = choice(title_pattern) +pronounce[windex([3,1,6])] +choice(tense1)+ age + choice(feature_tail) + Modal[windex([2,8])]
    return age_raw2, age

def age_type3():
    year_pattern = date_yearmd()
    age_raw3 = choice(title_pattern1) + year_pattern + choice(born_pattern)+ choice(attribute)
    return age_raw3, year_pattern

def age_type4():
    age = str(genageCN(18, 65))
    born_time = pronounce1[windex([1,1,1,1,1,1,4])]
    if born_time == '':
        age_raw4 = choice(title_pattern) +age+ choice(feature_tail) +choice(Modal)
    else:
        age_raw4 = choice(title_pattern) + born_time+ tense2[windex([2,8])]+age+ choice(feature_tail) +choice(Modal)
    return age_raw4, age

def age_type5():
    age = str(genageCN(18, 65))
    age_list = ['年龄是','岁数是']
    age_raw = '我的'+ age_list[windex([2,1])]+age +choice(['岁', ''])

def gen_age():
    age_list =[age_type1(), age_type2(),  age_type4(),age_type5()]
    age_ref, age_write = age_list[windex([4, 4, 1, 1])]
    return age_ref, age_write

def gen_year_age():
    age_ref, age_write =age_type3()
    return age_ref, age_write

if __name__ == "__main__":
    num_data = 2000
    list_data = list()
    label_name = 'age'
    for i in range(num_data):
        list_dict = dict()
        list_dict['label_name'] = label_name
        list_dict['id'] = i
        list_dict['ref'], list_dict['write'] = gen_year_age()
        list_data.append(list_dict)
        print('loading')
    obj = json.dumps(list_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/'+label_name+'_year_gen_0502_'+str(num_data)+'.json', 'w')
    file.write(obj)
    file.close()
