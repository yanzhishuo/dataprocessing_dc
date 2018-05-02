from weight_choice import *
from random import *
import json
import xlrd
import xlwt
from xlutils.copy import copy

#type 1
Modal = ['', '啊', '哦']
title_pattern = ['', '我', '我的']
pronounce = ['那个', '']
feature = ['户籍', '户籍地', '户籍地址', '老家']
verb = ['是', '就是', '在', '']
attribute = ['的', '']

#type 2
title_pattern2 = ['', '我']
verb2 = ['是', '']
tail = ['人', '']

data = xlrd.open_workbook('province.xlsx')
sheet_1_by_name=data.sheet_by_name('province_cities')
n_of_rows=sheet_1_by_name.nrows
n_of_cols=sheet_1_by_name.ncols
pro_city = list()
for i in range(1,n_of_rows):
    cell_A=sheet_1_by_name.row(i)[0].value
    cell_B=sheet_1_by_name.row(i)[1].value
    if cell_A !='':
        pro_city.append(cell_A)
    if cell_B !='':
        pro_city.append(cell_B)

# print(pro_city)
print(len(pro_city))

def census_type1():
    census_raw1_verb = verb[windex([4,1,2,3])]
    census_add1 = choice(pro_city)
    census_raw1 = Modal[windex([9,0.5,0.5])]+choice(title_pattern) +pronounce[windex([1,9])] +feature[windex([3,3,3,1])] +census_raw1_verb + census_add1
    if census_raw1_verb == '在':
        census_raw1 = census_raw1 + ''
    else:
        census_raw1 = census_raw1 + attribute[windex([1,9])]
    return census_raw1, census_add1

def census_type2():
    census_add2 = choice(pro_city)
    census_raw2 = Modal[windex([9.5,0.3,0.2])]+title_pattern2[windex([7,3])]+verb2[windex([3,7])]+census_add2+tail[windex([3,7])]
    return census_raw2, census_add2

def census_type3():
    return choice(pro_city)

def gen_census():
    census_list =[census_type1(), census_type2()]
    census_ref, census_write = census_list[windex([8,2])]
    return census_ref, census_write

if __name__ =="__main__":
    num_data = 50000
    census_data = list()
    for i in range(num_data):
        census_dict = dict()
        census_dict['label_name'] = 'census'
        census_dict['id'] = i
        census_dict['ref'],census_dict['write'] = gen_census()
        census_data.append(census_dict)
    obj = json.dumps(census_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/census_gen_0423_50000.json', 'w')
    file.write(obj)
    file.close()
