from random import *
import json
from weight_choice import *
from genpassword import *
from pyexcel import *
from classifyaddress import *
import re

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
# pro_city_county = readexcel(5, 'provincecc.xlsx')
county = readexcel(2, 'provincecc.xlsx')

def cut(data):
    if '省直辖县级行政区划' in data:
        pro1 = re.match('(\w{,2}省)?(.*省直辖县级行政区划)?(.*[林区|岛])?(.+[县|市])?', data)
    else:
        pro1 = re.match('(.*省)?(.*自治区)?(.*行政区)?(\w{,4}市)?(.*自治州)?(.*地区)?(.*[盟|区])?(.*市)?(.*旗)?(.+[县|市])?', data)


    pc = list()
    for x in pro1.groups():
        if x != None:
            pc.append(x)
    pccpc= str()
    for x in range(0,len(pc)-1):
        pccpc=pccpc+pc[x]
    pcc = list()
    for x in pro1.groups():
       if x != None:
           pcc.append(x)
    return pcc[0], pcc[1], pcc[2],pccpc
from gencensus.census0530 import *
pro_city_county_other,chuan,yue,zhe,su=choicemain()
pro_city_county = zhe
def census_type1():
    census_raw1_verb = verb[windex([4,1,2,3])]
    census_address1= choice(pro_city_county)
    print(census_address1+'1')
    census_province, census_city,census_county,census_pc= cut(census_address1)
    census_county_choice = choice(county)
    census_fc = [census_county_choice, '']
    census_cfc = census_fc[windex([1,3])]
    if census_cfc == census_county or census_cfc == '':
        census_add1 = census_pc
        m_county = 2
    else:
        census_add1 = census_pc +census_county_choice
        m_county = 0
    census_raw1 = Modal[windex([9,0.5,0.5])]+choice(title_pattern) +pronounce[windex([1,9])] +feature[windex([3,3,3,1])] +census_raw1_verb + census_add1
    if census_raw1_verb == '在':
        census_raw1 = census_raw1 + ''
    else:
        census_raw1 = census_raw1 + attribute[windex([1,9])]
    return census_raw1, census_address1, census_province, census_city,census_county,m_county

def census_type2():
    census_address2 = choice(pro_city_county)
    print(census_address2+'2')
    census_province, census_city,census_county,census_pc= cut(census_address2)
    census_county_choice = choice(county)
    census_fc = [census_county_choice, '']
    census_cfc = census_fc[windex([3,1])]
    if census_cfc == census_county or census_cfc == ''  :
        census_add2 = census_pc
        m_county = 2
    else:
        census_add2 = census_pc + census_county_choice
        m_county = 0
    census_raw2 = Modal[windex([9.5,0.3,0.2])]+title_pattern2[windex([7,3])]+verb2[windex([3,7])]+census_add2+tail[windex([3,7])]
    return census_raw2, census_address2, census_province, census_city,census_county,m_county

def gen_census():
    index = choice([0,1])
    census_list =[census_type1(), census_type2()]
    census_ref, census_write,  census_province, census_city,census_county,m_county=census_list[index]
    return census_ref, census_write, census_province, census_city,census_county,m_county

if __name__ =="__main__":
    num_data = 300
    # num_data = 2
    census_data = list()
    for i in range(num_data):
        census_dict = dict()
        census_dict['label_name'] = 'census'
        census_dict['id'] = i
        census_dict['ref'],census_dict['write'],census_dict['province'], census_dict['city'], census_dict['county'], census_dict['m_county'] = gen_census()
        census_dict['m_province'] = 1
        census_dict['m_city'] = 1
        census_data.append(census_dict)
    # print(census_data)
    obj = json.dumps(census_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/gendata/4_phone_census/zhe/census_proc_gen_0530_' + str(num_data) + '.json', 'w')
    file.write(obj)
    file.close()