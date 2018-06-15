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

class Appendneed():
    def __init__(self):
        self.items_list = str()
        self.items_choice = str()

    def update(self, iterable):
        self.items_list = ''.join(iterable)
        return self.items_list

    def choose(self, iterable):
        self.items_choice =choice(iterable)
        return self.items_choice

    def choose_append(self,iterable):
        for item in iterable:
            item1 = choice(item)
            self.items_list = self.items_list + item1
        return self.items_list

def need_choose(index,path):
    brand = readexcel(index, path)
    return brand
#直辖市
def city_county(index1,index2,index3,path):
    province = need_choose(index1,path)
    city = need_choose(index2,path)
    county = need_choose(index3,path)
    num_data = len(city)
    census_data = list()
    for i in range(num_data):
        C = Appendneed()
        a=C.choose_append([Modal,title_pattern,pronounce,feature,verb,[city[i]],[county[i]],attribute])
        b = province[i]+ city[i] + county[i]
        census_dict = dict()
        census_dict['label_name'] = 'census'
        census_dict['id'] = i
        census_dict['ref'] = a
        census_dict['write'] = b
        census_dict['m_city'],census_dict['m_county'],census_dict['m_province'] = 1,1,2
        census_dict['province_w'], census_dict['city_w'], census_dict['county_w'] = province[i],city[i],county[i]
        census_data.append(census_dict)
    # print(census_data)
    obj = json.dumps(census_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/census_citycounty_gen_0515_'+str(num_data)+'.json', 'w')
    file.write(obj)
    file.close()

def municipalities_city_county(index2,index3,path):
    # province = need_choose(index1,path)
    city = need_choose(index2,path)
    county = need_choose(index3,path)
    num_data = len(city)
    census_data = list()
    for i in range(num_data):
        C = Appendneed()
        a=C.choose_append([Modal,title_pattern,pronounce,feature,verb,[city[i]],[county[i]],attribute])
        b = city[i] + county[i]
        census_dict = dict()
        census_dict['label_name'] = 'census'
        census_dict['id'] = i
        census_dict['ref'] = a
        census_dict['write'] = b
        census_dict['m_city'],census_dict['m_county'],census_dict['m_province'] = 1,1,2
        census_dict['province_w'], census_dict['city_w'], census_dict['county_w'] ='',city[i],county[i]
        census_data.append(census_dict)
    # print(census_data)
    obj = json.dumps(census_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/census_citycounty_gen_0515_'+str(num_data)+'.json', 'w')
    file.write(obj)
    file.close()

if __name__ =="__main__":
    # municipalities_city_county(0,1,'../municipalities.xlsx')
    # a = Appendneed()
    # print(a.choose_append([Modal,title_pattern,pronounce]))
    # print(choice(['123']))
    # city_county(0,1,2,'../countylevelcity.xlsx')
    city_county(0,1,2,'../pccfinal.xlsx')
