from pyexcel import *
import json
from random import *
from weight_choice import *
import re

pro_city = readexcel(5, 'provincecc.xlsx')
# city = readexcel(1, '../provincecc.xlsx')
# county = readexcel(2, '../provincecc.xlsx')
# city_county = readexcel(9, '../provincecc.xlsx')
# county_mu = readexcel(8, '../provincecc.xlsx')
# municipalities = readexcel(7, '../provincecc.xlsx')

def choicemain():
    pro_city_county_main = []
    pro_city_county_other = []
    yue =[]
    zhe=[]
    su=[]
    for e in pro_city:
        if e[0:3] in ['四川省']:
            pro_city_county_main.append(e)
        elif e[0:3] in ['广东省']:
            yue.append(e)
        elif e[0:3] in ['浙江省']:
            zhe.append(e)
        elif e[0:3] in ['江苏省']:
            su.append(e)
        else:
            pro_city_county_other.append(e)
    return pro_city_county_other,pro_city_county_main,yue,zhe,su

