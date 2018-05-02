from random import *
import json
from weight_choice import *
from genpassword import *
from pyexcel import *

def get_address(index_c):
    data = dict()
    # province = openexcel(0, 'provincecc.xlsx')
    # city = openexcel(1, 'provincecc.xlsx')
    # county = openexcel(2, 'provincecc.xlsx')
    # pci = openexcel(3, 'provincecc.xlsx')
    # pct = openexcel(4, 'provincecc.xlsx')
    # pcc = openexcel(5, 'provincecc.xlsx')
    # cc = openexcel(6, 'provincecc.xlsx')
    # address_index = [0,1,2,3,4,5,6]
    # index_c = choice(address_index)
    add = openexcel(index_c, 'provincecc.xlsx')
    address_choice = add[1:]
    adc = choice(address_choice)
    if add[0] == '省':
        data['province'] = True
        data['county'] = False
        data['city'] = False
    elif add[0] == '市':
        data['city'] = True
        data['province'] = False
        data['county'] = False
    elif add[0] == '县':
        data['county'] = True
        data['province'] = False
        data['city'] = False
    elif add[0] == '省市' or adc in ['北京市', '重庆市', '上海市', '天津市']:
        data['province'] = True
        data['county'] = False
        data['city'] = True
    elif add[0] == '省县':
        data['province'] = True
        data['city'] = False
        data['county'] = True
    elif add[0] == '省市县' or adc in ['澳门特别行政区', '香港特别行政区','台湾省']:
        data['province'] = True
        data['city'] = True
        data['county'] = True
    else:
        data['province'] = False
        data['city'] = True
        data['county'] = True
    return data, adc

if __name__ == "__main__":
    print(get_address(0))


