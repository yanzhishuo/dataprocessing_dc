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

# path1 = '/home/yzs/Downloads/data_require/addressdetail/indetail.xlsx'
# path2 = '/home/yzs/Downloads/data_require/addressdetail/shandong.xlsx'
# path3 = '/home/yzs/Downloads/data_require/addressdetail/gansu.xlsx'
# c=excel2list(5,path1)
# d=excel2list(5,path2)
# e=excel2list(5,path3)
# address_list = c.getlist()+d.getlist()+e.getlist()#4279
# print(len(address_list))
# print((c.getlist()+d.getlist()+e.getlist())[1203])
# # x组x号  x单元x号 x排x号 2幢1单元4楼 第一户三楼 1单元4楼1号 4栋2单元311 7幢2组15号
community_add_detail1 = ['组','幢','单元','排','户','栋','巷','弄','门']
community_add_detail2 = ['楼','室','号']
county_add_detail1 = ['组','排']
county_add_detail2 = ['号','户']


# # print(addr_detail)
n = gennum(2,1,10)

#
# class add_choice():
#     def __init__(self,index):
#         self.index =index
#     def add_county(self):
#         add = list()
#         for i in range(self.index):
#             add.append(str(n.gennum())+choice(county_add_detail))
#         need = str()
#         for item in add:
#             need = need + item
#         return need
#     # def add_community(self):
#     #     add1 = str()
#     #     for i in range(self.index):
#     #         add1 + = n.gennum()+choice(community_add_detail)
#     #     return add1
#
# # hhh = add_choice(2)
# # print(hhh.add_county())
#
def add_county(index):
    num_gen = str(n.gennum())
    if index==1:
        add_county = num_gen +choice(county_add_detail1+county_add_detail2)
    else:
        num = choice([n.gennumpassword(), str(n.gennum())])
        add_county = str(n.gennum()) +choice(county_add_detail1) +num+choice(county_add_detail2)
    return add_county#,num_gen

def add_community(index):
    num_gen = str(n.gennum())
    if index ==1:
        add_community = num_gen +choice(community_add_detail1+community_add_detail2)
    elif index ==2:
        num = choice([n.gennumpassword(), str(n.gennum())])
        add_community =str(n.gennum())+ choice(community_add_detail1) + num + choice(community_add_detail2)
    else:
        # comm_a1 = choice(community_add_detail1)
        # add_community = num_gen + comm_a1
        # commu = copy.deepcopy(community_add_detail1)
        # commu.remove(comm_a1)
        com = random.sample(community_add_detail1,index-1)
        add1 = list()
        for item in com:
            add1.append(choice([n.gennumpassword(), str(n.gennum())])+item)
        add_community = str()
        for item in add1:
                add_community =  add_community+item
        add_community = add_community+n.gennumpassword()+choice(community_add_detail2)
    return add_community#,num_gen

# # print(add_county(choice([1,2])))
def genadd(addr_detail):
    if addr_detail[-1] == '村':
        small_address = add_county(choice([1,2]))
        addr_detail1 = addr_detail + small_address
    else:
        index_choice = [1,2,3]
        index = index_choice[windex([1,2,1])]
        small_address = add_community(index)
        addr_detail1 = addr_detail + small_address
    return addr_detail1

if __name__ == "__main__":
    # addr_detail = choice(address_list)
    num = 1000
    pro = list()
    for i in range(num):
        pro.append(add_county(choice([1, 2])))
    pro_city = []
    for item in pro:
        if item not in pro_city:
            pro_city.append(item)
    workbook = xlwt.Workbook(encoding = 'utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('Sheet1')
    # 写入excel
    # 参数对应 行, 列, 值
    worksheet.write(0,0, label = '组号')
    for i in range(1, len(pro_city) + 1):
        worksheet.write(i, 0, label = pro_city[i-1])
    # 保存
    workbook.save('detail_tail1.xlsx')


    # pro = list()
    # for i in range(num):
    #     # index_choice = [1, 2, 3]
    #     # index = index_choice[windex([1, 2, 1])]
    #     index = choice([1,2,3])
    #     pro.append(add_community(index))
    # pro_car = []
    # for item in pro:
    #     if item not in pro_car:
    #         pro_car.append(item)
    # data_1 = xlrd.open_workbook('detail_tail.xlsx')
    # wb = copy(data_1)
    # sheet = wb.get_sheet(0)
    # sheet.write(0,1, label = '区')
    # for i in range(1, len(pro_car)+1):
    #     sheet.write(i, 1, label=pro_car[i-1])
    # wb.save('detail_tail.xlsx')
