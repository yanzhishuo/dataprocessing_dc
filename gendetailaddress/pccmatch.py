from pyexcel import *
import json
from random import *
from gencensus.county import cut_mu
from weight_choice import *
import re
from gendetailaddress.group_pro import *

pro_city_county = readexcel(5, '../provincecc.xlsx')
city = readexcel(1, '../provincecc.xlsx')
county = readexcel(2, '../provincecc.xlsx')
city_county = readexcel(9, '../provincecc.xlsx')
county_mu = readexcel(8, '../provincecc.xlsx')
municipalities = readexcel(7, '../provincecc.xlsx')

def choicepcc():
    pro_city_county_main = []
    pro_city_county_other = []
    for e in pro_city_county:
        if e[0:3] in ['四川省','广东省','江苏省','浙江省']:
            pro_city_county_main.append(e)
        else:
            pro_city_county_other.append(e)
    return pro_city_county_other,pro_city_county_main

def cut(data):
    if '省直辖县级行政区划' in data:
        pro1 = re.match('(\w{,2}省)?(.*省直辖县级行政区划)?(.*[林区|岛])?(.+[县|市])?', data)
    else:
        pro1 = re.match('(.*省)?(.*自治区)?(.*行政区)?(\w{,4}市)?(.*自治州)?(.*地区)?(.*[盟|区])?(.*市)?(.*旗)?(.+[县|市])?', data)

    pcc = list()
    for x in pro1.groups():
        if x != None:
            pcc.append(x)
    return pcc[0], pcc[1], pcc[2]

def pccmatch(pro_city_county,index):
    if index ==1:
        census_add1 = choice(pro_city_county)
        census_province, census_city, census_county = cut(census_add1)
        census_out = census_add1
        m_province = 1
        m_city = 1
        m_county = 1
    elif index ==2:
        census_add1 = choice(pro_city_county)
        census_province, census_city, census_county = cut(census_add1)
        m_province = 1
        m_city = 2
        m_county = 2
        census_out = census_province
    elif index ==3:#市对（包括北京市等直辖市）
        a = choice([1,2])
        if a == 1:
            census_add1 = choice(pro_city_county)
            census_province, census_city, census_county = cut(census_add1)
            census_out = census_city
            m_province = 2
            m_city = 1
            m_county = 2
        else:
            census_add1 = choice(city_county)
            census_city, census_county = cut_mu(census_add1)
            census_out=census_city
            census_province=''
            m_province=''
            m_city=1
            m_county=2
    elif index ==4:#县对（包括北京市等直辖市）
        a = choice([1, 2])
        if a == 1:
            census_add1 = choice(pro_city_county)
            census_province, census_city, census_county = cut(census_add1)
            census_out = census_county
            m_province = 2
            m_city = 2
            m_county = 1
        else:
            census_add1 = choice(city_county)
            census_city, census_county = cut_mu(census_add1)
            census_out = census_county
            census_province = ''
            m_province = ''
            m_city = 2
            m_county = 1
    elif index==5:#省市对
        census_add1 = choice(pro_city_county)
        census_province, census_city, census_county = cut(census_add1)
        census_out = census_province+census_city
        m_province = 1
        m_city = 1
        m_county = 2
    elif index ==6:#市县对（包括北京市等直辖市）
        a = choice([1, 2])
        if a == 1:
            census_add1 = choice(pro_city_county)
            census_province, census_city, census_county = cut(census_add1)
            census_out = census_city+census_county
            m_province = 2
            m_city = 1
            m_county = 1
        else:
            census_add1 = choice(city_county)
            census_city, census_county = cut_mu(census_add1)
            census_out = census_add1
            census_province = ''
            m_province = ''
            m_city = 1
            m_county = 1
    else:#省县对
        census_add1 = choice(pro_city_county)
        census_province, census_city, census_county = cut(census_add1)
        census_out = census_province+census_county
        m_province = 1
        m_city = 2
        m_county = 1
    return census_add1,census_out,census_province,census_city,census_county,m_province,m_city,m_county

# def removeunwant():
group =group_by_province()
group_mu = group_by_mu()
def pccnomatch(index):
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    b1, b2 = sample(a, 2)
    census_add1, census_add2 = group[b1], group[b2]
    census_province1, census_city1, census_county1 = cut(choice(census_add1))
    census_province2, census_city2, census_county2 = cut(choice(census_add2))
    c = [0,1,2,3]
    d1, d2 = sample(c, 2)
    census_add3, census_add4 = group_mu[d1], group_mu[d2]
    census_city3, census_county3 =cut_mu(choice(census_add3))
    census_city4, census_county4 = cut_mu(choice(census_add4))
    if index ==1:#省不匹配
        a_index = choice([1, 2,3,4])
        if a_index == 1:
            census_out = census_province2+census_city1+census_county1
            m_province = 0
            m_city = 1
            m_county = 1
        elif a_index ==2:
            census_out = census_province2 + census_city1
            m_province = 0
            m_city = 1
            m_county = 2
        elif a_index ==3:
            census_out = census_province2 + census_county1
            m_province = 0
            m_city = 2
            m_county = 1
        else:
            census_out = census_province2
            m_province = 0
            m_city = 2
            m_county = 2

    elif index ==2:#市不匹配（包括北京市等直辖市）
        a_index = choice([1, 2])
        if a_index == 1:
            b_index = choice([1, 2, 3, 4])
            if b_index == 1:
                census_out = census_province1 + census_city2 + census_county1
                m_province = 1
                m_city = 0
                m_county = 1
            elif b_index == 2:
                census_out = census_province1 + census_city2
                m_province = 1
                m_city = 0
                m_county = 2
            elif b_index == 3:
                census_out = census_city2 + census_county1
                m_province = 2
                m_city = 0
                m_county = 1
            else:
                census_out = census_city2
                m_province = 2
                m_city = 0
                m_county = 2
        else:
            b_index = choice([1, 2])
            if b_index == 1:
                census_out =  census_city4 + census_county3
                m_province = ''
                m_city = 0
                m_county = 1
            else:
                census_out = census_city4
                m_province = ''
                m_city = 0
                m_county = 2

    elif index ==3:#县不匹配（包括北京市等直辖市）
        a_index = choice([1,2])
        if a_index == 1:
            b_index = choice([1, 2, 3, 4])
            if b_index == 1:
                census_out = census_province1 + census_city1 + census_county2
                m_province = 1
                m_city = 1
                m_county = 0
            elif b_index == 2:
                census_out = census_province1 + census_county2
                m_province = 1
                m_city = 2
                m_county = 0
            elif b_index == 3:
                census_out = census_city1 + census_county2
                m_province = 2
                m_city = 1
                m_county = 0
            else:
                census_out = census_county2
                m_province = 2
                m_city = 2
                m_county = 0
        else:
            b_index = choice([1, 2])
            if b_index == 1:
                census_out = census_city3 + census_county4
                m_province = ''
                m_city = 1
                m_county = 0
            else:
                census_out = census_county4
                m_province = ''
                m_city = 2
                m_county = 0
    elif index ==4:#省市县都不匹配
        census_out = census_province2+census_city2+census_county2
        m_province = 0
        m_city = 0
        m_county = 0

    elif index==5:#省市不匹配
        b_index = choice([1, 2])
        if b_index == 1:
            census_out = census_province2+census_city2+census_county1
            m_province = 0
            m_city = 0
            m_county = 1
        else:
            census_out = census_province2 + census_city2
            m_province = 0
            m_city = 0
            m_county = 2
    elif index ==6:#市县不匹配（包括北京市等直辖市）
        a_index = choice([1, 2])
        if a_index == 1:
            b_index = choice([1, 2])
            if b_index == 1:
                census_out = census_province1+census_city2+census_county2
                m_province = 1
                m_city = 0
                m_county = 0
            else:
                census_out =  census_city2 + census_county2
                m_province = 2
                m_city = 0
                m_county = 0
        else:
            census_out = census_city4+census_county4
            m_province = ''
            m_city = 0
            m_county = 0
    else:#省县不匹配
        a_index = choice([1, 2])
        if a_index == 1:
            census_out = census_province2 + census_city1 + census_county2
            m_province = 0
            m_city = 1
            m_county = 0
        else:
            census_out = census_province2  + census_county2
            m_province = 0
            m_city = 2
            m_county = 0
    if m_province !='':
        return census_province1+census_city1+census_county1,census_out,census_province1,census_city1,census_county1,m_province,m_city,m_county
    else:
        return census_city3+census_county3,census_out,'',census_city3,census_county3,'',m_city,m_county

def mainmatch(index):
    other, main = choicepcc()
    if index==1:
        a=pccmatch(main, choice([1, 2, 3, 4, 5, 6, 7]))
    else:
        a=pccmatch(other, choice([1, 2, 3, 4, 5, 6, 7]))
    return a
#省市县都对
#省对
#市对（包括北京市等直辖市）
#县对（包括北京市等直辖市）
#省市对
#市县对（包括北京市等直辖市）
#省县对
if __name__=="__main__":
    # # other, main = choicepcc()
    # # for i in range(10):
    # #     print(pccmatch(main,choice([1,2,3,4,5,6,7])))
    for i in range(10):
        # print(pccmatch(other,choice([1,2,3,4,5,6,7])))
        a=choice([1,2,3,4,5,6,7])
        print(a)
        print(pccnomatch(a))
