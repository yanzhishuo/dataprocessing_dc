from random import *
import re
import json
from weight_choice import *
from pyexcel import *
from datetime import datetime
from gendata.inherit import *
import xlrd
import xlwt
from xlutils.copy import copy
# import copy #deepcopy
from gendetailaddress.pccmatch import *
from gendetailaddress.detailmatch import *
from gendetailaddress.roadmatch import *

#您公司的地址在哪里
head =['','啊','额','那个','就知道']
company = ['','我公司地址','我公司的地址','我的公司地址','地址','公司地址','公司']
verb =['','是','在','就在']
#您工作单位地址是哪里
# head =['','啊','额','那个','就','就知道']
company1 = ['','我工作单位地址','我单位的地址','我的工作地址','地址','单位地址','工作单位','单位']
# verb =['','是','在']
#type 1
Modal = ['', '','','啊', '哦']
title_pattern = ['', '我', '我的']
pronounce = ['那个', '','']
feature = ['户籍', '户籍地', '户籍地址', '地址','老家']
verb_census = ['是', '就是', '在','就在', '']
attribute = ['的', '']

#type 2
title_pattern2 = ['', '我']
verb2 = ['是', '']
tail = ['人', '']
#地址组成：省市县（省或者县或者市说一个两个都对）+路/大厦（没有号也对）（不是全部对吗？）
#main 省市县#other 省市县
l=[1,2]
# print(mainmatch(l[windex([4,1])]))
# def addressjson(large_address,medium_address,small_address,ref,m_roaddetail,m_small=1,m_medium=1,m_large=1):
def addressjson(i,large_address,pcc_province,pcc_city,pcc_county,m_province,m_city,m_county,medium_address,small_address,ref,m_small=1,m_medium=1,m_large=1):
        census_dict = dict()
        census_dict['label_name'] = 'address'
        census_dict['id'] = i
        census_dict['ref']=ref
        census_dict['write']=large_address+medium_address+small_address
        census_dict['m_large']=m_large
        census_dict['m_medium'] = m_medium
        census_dict['m_small'] = m_small
        census_dict['large_address']=large_address
        census_dict['medium_address'] = medium_address
        census_dict['small_address'] = small_address
        census_dict['m_province'] = m_province
        census_dict['m_city'] = m_city
        census_dict['m_county'] = m_county
        census_dict['province'] = pcc_province
        census_dict['city'] = pcc_city
        census_dict['county'] = pcc_county
        # census_dict['road_detail'] = m_roaddetail
        return census_dict

num_data = 1000
def genrightaddress(a,b,c,num_data,pattern ='right'):
    # num = 1
    for num in range(1,4):
        census_data = list()
        for i in range(num_data):
            pcc_write,pcc_ref,pcc_province,pcc_city,pcc_county,m_province,m_city,m_county=mainmatch(choice([1,1,1,1,2]))
            road_write, road_ref,road,road_detail,m_road,m_roaddetail = roadmatch(choice([1,1,2]))
            building_write,building_ref,building,building_detail,m_building,m_buildingdetail=detailaddress([1,2,3,4][windex([3,2,1,1])])
            # print(num)
            if num == 1:
                census_dict = addressjson(i,pcc_write,pcc_province,pcc_city,pcc_county,m_province,m_city,m_county,road_write,building_write,choice(a)+choice(b)+choice(c)+pcc_ref+road_ref+building_ref)
            elif num ==2:
                census_dict = addressjson(i,pcc_write,pcc_province,pcc_city,pcc_county,m_province,m_city,m_county,road_write,building_write,choice(a)+choice(b)+choice(c)+pcc_ref+building_ref,m_medium=2)#m_medium为空
            else:
                census_dict = addressjson(i,pcc_write,pcc_province,pcc_city,pcc_county,m_province,m_city,m_county,road_write,building_write,choice(a)+choice(b)+choice(c)+pcc_ref+road_ref,m_small=2)#m_small为空
            census_data.append(census_dict)
        print(census_data)
        obj = json.dumps(census_data, ensure_ascii=False, indent=2)
        file = open('/home/yzs/gendata/daqige/census_50000/address/'+'address_company_'+pattern+'_gen_'+str(datenow())+'_' + str(num_data)+'_' + str(num) + '.json', 'w')
        file.write(obj)
        file.close()

def genrightproaddress(a,b,c,path,pattern ='detail_wrong'):
    for num in range(4,10):
        census_data = list()
        for i in range(num_data):
            pcc_write,pcc_ref,pcc_province,pcc_city,pcc_county,m_province,m_city,m_county=mainmatch(choice([1,1,2]))
            road_write, road_ref,road,road_detail,m_road,m_roaddetail = roadmatch(choice([1,1,2]))
            road_write0, road_ref0, road0, road_detail0, m_road0 = roadnomatch(choice([1, 1, 2]))
            building_write,building_ref,building,building_detail,m_building,m_buildingdetail=detailaddress([1,2,3,4][windex([3,2,1,1])])
            building_write0, building_ref0, building0, building_detail0, m_buildingdetail0 = detailnomatch([1, 2, 3, 4][windexint([3, 2, 1, 1])])
            if num ==4:
                census_dict = addressjson(i,pcc_write,road_write0,building_write,choice(a)+choice(b)+choice(c)+pcc_ref+road_ref0,m_small=2,m_medium=0)
            elif num ==5:
                census_dict = addressjson(i,pcc_write,road_write,building_write0,choice(a)+choice(b)+choice(c)+pcc_ref+building_ref0,m_medium=2,m_small=0)#m_medium为空
            elif num ==6:
                census_dict = addressjson(i,pcc_write,road_write0,building_write0,choice(a)+choice(b)+choice(c)+pcc_ref+road_ref0+building_ref0,m_small=0,m_medium=0)
            elif num ==7:
                census_dict = addressjson(i,pcc_write,road_write0,building_write,choice(a)+choice(b)+choice(c)+pcc_ref+road_ref0+building_ref,m_medium=0)
            elif num ==8:
                census_dict = addressjson(i,pcc_write,road_write,building_write0,choice(a)+choice(b)+choice(c)+pcc_ref+road_ref+building_ref0,m_medium=1,m_small=0)
            else:
                census_dict = addressjson(i,pcc_write,road_write,building_write,choice(a)+choice(b)+choice(c)+pcc_ref,m_medium=2,m_small=2)

def censusjson(i, province,city,county,ref, m_small=1, m_medium=1, m_large=1):
        census_dict = dict()
        census_dict['label_name'] = 'census'
        census_dict['id'] = i
        census_dict['ref'] = ref
        census_dict['write'] = province+city+county
        census_dict['m_province'] = m_large
        census_dict['m_city'] = m_medium
        census_dict['m_county'] = m_small
        census_dict['province'] = province
        census_dict['city'] = city
        census_dict['county'] = county
        # census_dict['road_detail'] = m_roaddetail
        return census_dict

def gencensusonly(num_data,pattern ='census_only'):
    census_data = list()
    for i in range(num_data):
        pcc_write, pcc_ref, pcc_province, pcc_city, pcc_county, m_province, m_city, m_county = mainmatch(choice([1,1,1,1,2]))
        census_dict = censusjson(i, pcc_province,pcc_city,pcc_county,
                                  choice(Modal) + choice(title_pattern) + choice(
                                      pronounce) +choice(feature)+choice(verb_census)+ pcc_ref+choice(attribute),
                                 m_county,m_city,m_province)
        # census_dict = censusjson(i, pcc_province, pcc_city, pcc_county,
        #                          choice(title_pattern2) + choice(verb2)+pcc_ref + choice(tail),
        #                          m_county, m_city, m_province)
        census_data.append(census_dict)
    print(census_data)
    obj = json.dumps(census_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/gendata/daqige/census_50000/census' + '/census_' + pattern + '_gen_' + str(datenow()) + '_' + str(num_data)+'.json', 'w')
    file.write(obj)
    file.close()

def genrightcensus(num_data,path,pattern ='detail'):
    # num = 1
    for num in range(1,4):
        census_data = list()
        for i in range(num_data):
            pcc_write,pcc_ref,pcc_province,pcc_city,pcc_county,m_province,m_city,m_county=mainmatch(choice([1,1,1,1,2]))
            road_write, road_ref,road,road_detail,m_road,m_roaddetail = roadmatch(choice([1,1,2]))
            building_write,building_ref,building,building_detail,m_building,m_buildingdetail=detailaddress([1,2,3,4][windex([3,2,1,1])])
            # print(num)
            if num == 1:
                census_dict = addressjson(i,pcc_write,road_write,building_write,choice(a)+choice(b)+choice(c)+pcc_ref+road_ref+building_ref)
            elif num ==2:
                census_dict = addressjson(i,pcc_write,road_write,building_write,choice(a)+choice(b)+choice(c)+pcc_ref+building_ref,m_medium=2)#m_medium为空
            else:
                census_dict = addressjson(i,pcc_write,road_write,building_write,choice(a)+choice(b)+choice(c)+pcc_ref+road_ref,m_small=2)#m_small为空
            census_data.append(census_dict)
        print(census_data)
        obj = json.dumps(census_data, ensure_ascii=False, indent=2)
        file = open('/home/yzs/gendata/5_phone_address/'+path+'/address_'+pattern+'_gen_'+str(datenow())+'_' + str(num_data)+'_' + str(num) + '.json', 'w')
        file.write(obj)
        file.close()


if __name__=="__main__":
    genrightaddress(head,company,verb,5000)
    # num_data = 5000
    # for num in range(1,4):
    #     census_data = list()
    #     for i in range(num_data):
    #         pcc_write,pcc_ref,pcc_province,pcc_city,pcc_county,m_province,m_city,m_county=mainmatch(choice([1,1,1,1,2]))
    #         road_write, road_ref,road,road_detail,m_road,m_roaddetail = roadmatch(choice([1,1,2]))
    #         building_write,building_ref,building,building_detail,m_building,m_buildingdetail=detailaddress([1,2,3,4][windex([3,2,1,1])])
    #         # print(num)
    #         if num == 1:
    #             census_dict = addressjson(i,pcc_write,pcc_province,pcc_city,pcc_county,m_province,m_city,m_county,road_write,building_write,choice(Modal)+choice(title_pattern)+choice(pronounce)+choice(feature)+choice(verb_census)+pcc_ref+road_ref+building_ref+choice(attribute))
    #         elif num ==2:
    #             census_dict = addressjson(i,pcc_write,pcc_province,pcc_city,pcc_county,m_province,m_city,m_county,road_write,building_write,choice(Modal)+choice(title_pattern)+choice(pronounce)+choice(feature)+choice(verb_census)+pcc_ref+building_ref+choice(attribute),m_medium=2)#m_medium为空
    #         else:
    #             census_dict = addressjson(i,pcc_write,pcc_province,pcc_city,pcc_county,m_province,m_city,m_county,road_write,building_write,choice(Modal)+choice(title_pattern)+choice(pronounce)+choice(feature)+choice(verb_census)+pcc_ref+road_ref+choice(attribute),m_small=2)#m_small为空
    #         census_data.append(census_dict)
    #     print(census_data)
    #     obj = json.dumps(census_data, ensure_ascii=False, indent=2)
    #     file = open('/home/yzs/gendata/daqige/census_50000/census/'+'address_gen_'+str(datenow())+'_' + str(num_data)+'_' + str(num) + '.json', 'w')
    #     file.write(obj)
    #     file.close()
    #gencensusonly(15000)
    # #right
    # num_data = 1000
    # num = 1
    # census_data = list()
    # for i in range(num_data):
    #     pcc_write,pcc_ref,pcc_province,pcc_city,pcc_county,m_province,m_city,m_county=mainmatch(choice([1,1,2]))
    #     road_write, road_ref,road,road_detail,m_road,m_roaddetail = roadmatch(choice([1,1,2]))
    #     building_write,building_ref,building,building_detail,m_building,m_buildingdetail=detailaddress([1,2,3,4][windex([3,2,1,1])])
    #     census_dict = addressjson(pcc_write,road_write,building_write,choice(head)+choice(company1)+choice(verb)+pcc_ref+road_ref+building_ref,m_roaddetail)
    #     # census_dict = addressjson(pcc_write,road_write,building_write,choice(head)+choice(company)+choice(verb)+pcc_ref+building_ref,m_medium=2)#m_medium为空
    #     # census_dict = addressjson(pcc_write,road_write,building_write,choice(head)+choice(company)+choice(verb)+pcc_ref+road_ref,m_small=2)#m_small为空
    #     census_data.append(census_dict)
    #     # print(census_data)
    # obj = json.dumps(census_data, ensure_ascii=False, indent=2)
    # file = open('/home/yzs/gendata/5_phone_address/empty/address_right_gen_'+str(datenow())+'_' + str(num_data)+'_' + str(num) + '.json', 'w')
    # file.write(obj)
    # file.close()

    # #mddium or small wrong
    # num_data = 1000
    # num = 8
    # census_data = list()
    # for i in range(num_data):
    #     pcc_write, pcc_ref, pcc_province, pcc_city, pcc_county, m_province, m_city, m_county = mainmatch(choice([1, 1, 2]))
    #     # road_write, road_ref, road, road_detail, m_road = roadnomatch(choice([1, 1, 2]))
    #     road_write, road_ref, road, road_detail, m_road, m_roaddetail = roadmatch(choice([1, 1, 2]))
    #     building_write, building_ref, building, building_detail, m_building, m_buildingdetail = detailaddress([1, 2, 3, 4][windexint([3, 2, 1, 1])])
    #     # building_write, building_ref, building, building_detail, m_buildingdetail = detailnomatch([1, 2, 3, 4][windexint([3, 2, 1, 1])])
    #     census_dict = addressjson(pcc_write,road_write,building_write,choice(head)+choice(company)+choice(verb)+building_ref,m_small=1,m_medium=2,m_large=2)
    #     # census_dict = addressjson(pcc_write,road_write,building_write,pcc_ref,m_small=2,m_medium=2)
    #     # census_dict = addressjson(pcc_write, road_write, building_write, pcc_ref + road_ref,m_small=2,m_medium=0)  # m_medium为空
    #     # census_dict = addressjson(pcc_write,road_write,building_write,pcc_ref+road_ref,m_small=2)#m_small为空
    #     census_data.append(census_dict)
    #     # print(census_data)
    # obj = json.dumps(census_data, ensure_ascii=False, indent=2)
    # file = open('/home/yzs/gendata/5_phone_address/address_no_province_wrong_gen_' + str(datenow()) + '_' + str(num_data) + '_' + str(num) + '.json', 'w')
    # file.write(obj)
    # file.close()

    # #province wrong
    # num_data = 1000
    # num = 5
    # census_data = list()
    # for i in range(num_data):
    #     pcc_write, pcc_ref, pcc_province, pcc_city, pcc_county, m_province, m_city, m_county = pccnomatch(choice([1,2,3,4,5,6,7]))
    #     # road_write, road_ref, road, road_detail, m_road = roadnomatch(choice([1, 1, 2]))
    #     road_write, road_ref, road, road_detail, m_road, m_roaddetail = roadmatch(choice([1, 1, 2]))
    #     building_write, building_ref, building, building_detail, m_building, m_buildingdetail = detailaddress([1, 2, 3, 4][windexint([3, 2, 1, 1])])
    #     # building_write, building_ref, building, building_detail, m_buildingdetail = detailnomatch([1, 2, 3, 4][windexint([3, 2, 1, 1])])
    #     # census_dict = addressjson(pcc_write,road_write,building_write,choice(head)+choice(company)+choice(verb)+pcc_ref+road_ref+building_ref,m_small=0,m_medium=0,m_large=0)
    #     census_dict = addressjson(pcc_write,road_write,building_write,choice(head)+choice(company)+choice(verb)+road_ref+building_ref,m_small=1,m_medium=1,m_large=2)
    #     # census_dict = addressjson(pcc_write,road_write,building_write,pcc_ref,m_small=2,m_medium=2)
    #     # census_dict = addressjson(pcc_write, road_write, building_write, pcc_ref + road_ref,m_small=2,m_medium=0)  # m_medium为空
    #     # census_dict = addressjson(pcc_write,road_write,building_write,pcc_ref+road_ref,m_small=2)#m_small为空
    #     census_data.append(census_dict)
    #     # print(census_data)
    # obj = json.dumps(census_data, ensure_ascii=False, indent=2)
    # file = open('/home/yzs/gendata/5_phone_address/address_no_province_wrong_gen_' + str(datenow()) + '_' + str(num_data) + '_' + str(num) + '.json', 'w')
    # file.write(obj)
    # file.close()
