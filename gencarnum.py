from random import *
import json
import xlrd
from genpassword import *
from pyexcel import *
from weight_choice import *
import string

title_pattern = ['', '我', '我的']
feature = ['车牌', '车牌号', '车牌号码', '号码', '']
verb = ['是', '好像是', '']
first_two = pyexcel(0,'/home/yzs/Downloads/data_require/carnum.xlsx')

def choosemain():
    abbreviation =[]
    yue=[]
    zhe=[]
    su=[]
    other = []
    for e in first_two:
        if e[0] in ['川']:
            abbreviation.append(e)
        elif e[0] in ['粤']:
            yue.append(e)
        elif e[0] in ['浙']:
            zhe.append(e)
        elif e[0] in ['苏']:
            su.append(e)
        else:
            other.append(e)
    return other,abbreviation,yue,zhe,su

def carnum_type(first_two):
    carnum_write = choice(first_two) + genpasswordcarnum(5,choice([2,3,4,5]))
    carnum_raw = title_pattern[windex([5.5,0.5,4])] + feature[windex([1,2,1,2,4])] + verb[windex([3,2,5])] + carnum_write
    return carnum_raw, carnum_write

if __name__ == "__main__":
    other,chuan,yue,zhe,su = choosemain()
    # print(len(other),len(main))
    num_data = 10000
    di = other
    carnum_data = list()
    for i in range(num_data):
        carnum_dict = dict()
        carnum_dict['label_name'] = 'carnum'
        carnum_dict['id'] = i
        carnum_dict['ref'],carnum_dict['write'] = carnum_type(di)
        carnum_data.append(carnum_dict)
    obj = json.dumps(carnum_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/gendata/phone_carnum/carnum_gen_0611_'+str(num_data)+'_other'+'.json', 'w')
    file.write(obj)
    file.close()



