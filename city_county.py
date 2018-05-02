from random import *
import re
import json
from weight_choice import *
from genpassword import *
from pyexcel import *
from classifyaddress import *

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
pro_city_county1 = readexcel(5, 'provincecc.xlsx')
pro_city_county = pro_city_county1[:2856]
province = readexcel(0, 'provincecc.xlsx')
city = readexcel(1, 'provincecc.xlsx')
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
    for x in range(1,len(pc)):
        pccpc=pccpc+pc[x]
    pcc = list()
    for x in pro1.groups():
       if x != None:
           pcc.append(x)
       if x in ['上海市', '重庆市', '天津市', '北京市']:
           pcc.append('直辖市')
    return pcc[0], pcc[1], pcc[2],pccpc

def census_type1():
    census_raw1_verb = verb[windex([4,1,2,3])]
    census_address1= choice(pro_city_county)
    print(census_address1+'1')
    census_province, census_city,census_county,census_pc= cut(census_address1)
    census_province_choice = choice(province)
    census_fc = [census_province_choice, '']
    census_cfc = census_fc[windex([1,1])]
    if census_cfc == census_province or census_cfc == '':
        census_add1 = census_pc
        m_province = 2
    else:
        census_add1 = census_province_choice + census_pc
        m_province = 0
    census_raw1 = Modal[windex([9,0.5,0.5])]+choice(title_pattern) +pronounce[windex([1,9])] +feature[windex([3,3,3,1])] +census_raw1_verb + census_add1
    if census_raw1_verb == '在':
        census_raw1 = census_raw1 + ''
    else:
        census_raw1 = census_raw1 + attribute[windex([1,9])]
    return census_raw1, census_address1, census_province, census_city,census_county,m_province

def census_type2():
    census_address2 = choice(pro_city_county)
    print(census_address2+'2')
    census_province, census_city, census_county, census_pc = cut(census_address2)
    census_province_choice = choice(province)
    census_fc = [census_province_choice, '']
    census_cfc = census_fc[windex([1, 1])]
    if census_cfc == census_province or census_cfc == '':
        census_add1 = census_pc
        m_province = 2
    else:
        census_add1 = census_province_choice + census_pc
        m_province = 0
    census_raw2 = Modal[windex([9.5,0.3,0.2])]+title_pattern2[windex([7,3])]+verb2[windex([3,7])]+census_add1+tail[windex([3,7])]
    return census_raw2, census_address2, census_province, census_city,census_county,m_province

def gen_census():
    index = choice([0,1])
    census_list =[census_type1(), census_type2()]
    census_ref, census_write,  census_province, census_city,census_county,m_province=census_list[index]
    return census_ref, census_write, census_province, census_city,census_county,m_province
if __name__ =="__main__":
    # data = '上海市浦东区'
    # data = '福建省宁德市福安市'
    # data = '北京市平谷区'
    # data = '吉林省延边朝鲜族自治州珲春市'
    # data =    '江西省九江地区瑞昌市'
    # print(cut('海南省省直辖县级行政区划白沙黎族自治县'))
    # print(cut('海南省省直辖县级行政区划西沙群岛'))
    # data = '海南省省直辖县级行政区划西沙群岛'
    # data = '海南省省直辖县级行政区划哈哈哈林区'
    # a,b=cut(data)
    # print(a,b)
    # num_data = 3000
    num_data = 2000
    census_data = list()
    for i in range(num_data):
        census_dict = dict()
        census_dict['label_name'] = 'census'
        census_dict['id'] = i
        census_dict['ref'],census_dict['write'],census_dict['province'], census_dict['city'], census_dict['county'], census_dict['m_province'] = gen_census()
        census_dict['m_county'] = 1
        census_dict['m_city'] = 1
        census_data.append(census_dict)
    # print(census_data)
    obj = json.dumps(census_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/census_citycounty_gen_0502_2000.json', 'w')
    file.write(obj)
    file.close()
