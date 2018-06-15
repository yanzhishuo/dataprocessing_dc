from pyexcel import *
import json
from random import *
from gencensus.county import cut_mu
from weight_choice import *
import re

pro_city_county = readexcel(5, '../provincecc.xlsx')
city_county = readexcel(9, '../provincecc.xlsx')

def group_by_province():
    hui=[]
    fujian =[]
    gansu=[]
    yue=[]
    gui =[]
    qian =[]
    qiong =[]
    ji =[]
    yu=[]
    hei =[]
    e =[]
    xiang =[]
    jilin=[]
    su=[]
    gan=[]
    liao=[]
    meng =[]
    ning =[]
    qing=[]
    lu =[]
    jin = []
    shan = []
    chuan =[]
    zang =[]
    xin =[]
    dian=[]
    zhe=[]

    for item in pro_city_county:
        if item[0:2] =='安徽':
            hui.append(item)
        elif item[0:2] =='福建':
            fujian.append(item)
        elif item[0:2] =='甘肃':
            gansu.append(item)
        elif item[0:2] =='广东':
            yue.append(item)
        elif item[0:2] =='广西':
            gui.append(item)
        elif item[0:2] =='贵州':
            qian.append(item)
        elif item[0:2] =='海南':
            qiong.append(item)
        elif item[0:2] =='河北':
            ji.append(item)
        elif item[0:2] =='河南':
            yu.append(item)
        elif item[0:2] =='湖北':
            e.append(item)
        elif item[0:2] =='湖南':
            xiang.append(item)
        elif item[0:2] =='吉林':
            jilin.append(item)
        elif item[0:2] =='江苏':
            su.append(item)
        elif item[0:2] =='江西':
            gan.append(item)
        elif item[0:2] =='辽宁':
            liao.append(item)
        elif item[0:2] =='内蒙':
            meng.append(item)
        elif item[0:2] =='宁夏':
            ning.append(item)
        elif item[0:2] =='青海':
            qing.append(item)
        elif item[0:2] =='山东':
            lu.append(item)
        elif item[0:2] =='山西':
            jin.append(item)
        elif item[0:2] =='陕西':
            shan.append(item)
        elif item[0:2] =='四川':
            chuan.append(item)
        elif item[0:2] =='西藏':
            zang.append(item)
        elif item[0:2] =='新疆':
            xin.append(item)
        elif item[0:2] =='云南':
            dian.append(item)
        elif item[0:2] =='浙江':
            zhe.append(item)
        else:
            hei.append(item)
    group = [hui,fujian,gansu,yue,gui,qian,qiong,ji,yu,hei,e,xiang,jilin,su,gan,liao,meng,ning,qing,lu,jin,shan,chuan,zang,xin,dian,zhe]
    return group

def group_by_mu():
    jing = []
    hu=[]
    jin=[]
    yu=[]
    for item in city_county:
        if item[0:2] =='北京':
            jing.append(item)
        elif item[0:2] =='上海':
            hu.append(item)
        elif item[0:2] =='天津':
            jin.append(item)
        else:
            yu.append(item)
    group = [jing,hu,jin,yu]
    return group

if __name__=="__main__":
    # print(choice(group_by_province()[0]))
    print(choice(group_by_mu()[0]))



