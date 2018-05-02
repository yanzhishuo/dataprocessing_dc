from random import *
import json
from weight_choice import *
from genpassword import *
from genbirth import *
import pyexcel
from pyexcel import readexcel
from listtojson import *

title_pattern = ['我','']
Modal = ['','啊']
attribute = ['','叫','是','的名字是']

parents = ['父亲','母亲','爸爸','妈妈','爸','妈','爹','娘','家父','家母']
love = ['爱人','妻子','老公','老婆','媳妇','丈夫','先生','夫人','太太','内人','相公']
namelist = pyexcel.readexcel(7,'/home/yzs/Downloads/data_require/final_new.xlsx')

def appellation():
    brother = choice(['表', '堂']) + choice(['哥', '兄', '弟', '姐', '妹'])
    Straight_brother = choice(['亲', '']) + choice(['哥', '弟', '姐', '妹', '哥哥', '弟弟', '姐姐', '妹妹'])
    cl = love[windex([7, 2, 2, 2, 1, 1, 0.5, 0.5, 0.5, 0.5, 0.5])]
    cp = parents[windex([4, 4, 2, 0.6, 0.6, 0.6, 0.1, 0.1, 0.1, 0.1])]
    choose_call = [cl, cp, brother,Straight_brother]
    appellation = choose_call[windex([3,3,1,2])]
    return appellation

def title():
    title = title_pattern[windex([2,8])]
    return title

def choose_Modal():
    choose_Modal = Modal[windex([9,1])]
    return choose_Modal

def choose_attr():
    choose_attr = attribute[windex([8,1,1,1])]
    return choose_attr

def name_type1():
    name = choice(namelist)
    name_raw1 = title() + appellation() + choose_Modal() +choose_attr() + name
    return name_raw1, name

def name_type2():
    name = choice(namelist)
    name_raw2 = choice(['他','她']) + choice(['叫','是','的名字是']) + choose_Modal()  + name
    return name_raw2, name

def name_type3():
    name = choice(namelist)
    name_raw3 = name + '是我' + appellation()
    return name_raw3, name

def name_type4():
    name = choice(namelist)
    cw = ['','叫','是','名字是']
    name_raw4 = cw[windex([5,1,1,1])]+name
    return name_raw4, name

def gen_name():
    name_typelist = [name_type1(), name_type2(), name_type3(), name_type4()]
    name_ref, name_write = name_typelist[windex([3,2,1,4])]
    return name_ref, name_write


if __name__ == "__main__":
    num_data = 10000
    list_data = list()
    label_name = 'name'
    for i in range(num_data):
        list_dict = dict()
        list_dict['label_name'] = label_name
        list_dict['id'] = i
        list_dict['ref'], list_dict['write'] = gen_name()
        list_data.append(list_dict)
        print('loading')
    obj = json.dumps(list_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/'+label_name+'_gen_0425_'+str(num_data)+'.json', 'w')
    file.write(obj)
    file.close()

