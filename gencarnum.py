from random import *
import json
import xlrd
from genpassword import *
from pyexcel import *
from weight_choice import *

title_pattern = ['', '我', '我的']
feature = ['车牌', '车牌号', '牌子', '车牌子', '']
verb = ['是', '好像是', '']
first_two = pyexcel(0,'/home/yzs/Downloads/data_require/carnum.xlsx')
last_five = genpassword(5)

def carnum_type():
    carnum_write = choice(first_two) +last_five
    carnum_raw = title_pattern[windex([5.5,0.5,4])] + feature[windex([1,2,1,2,4])] + verb[windex([3,2,5])] + carnum_write
    return carnum_raw, carnum_write

if __name__ == "__main__":
    num_data = 50000
    carnum_data = list()
    for i in range(num_data):
        carnum_dict = dict()
        carnum_dict['label_name'] = 'carnum'
        carnum_dict['id'] = i
        carnum_dict['ref'],carnum_dict['write'] = carnum_type()
        carnum_data.append(carnum_dict)
    obj = json.dumps(carnum_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/carnum_gen_0424_50000.json', 'w')
    file.write(obj)
    file.close()



