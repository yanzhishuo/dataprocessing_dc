from random import *
import json
from weight_choice import *
from genpassword import *
from pyexcel import *
from genpassword import *

head = ['','那个','我的车是','我的车辆品牌是','我的车品牌是','车牌子是','是','品牌是','牌子是']
# print([1]*len(head))
weight_head = [3, 2, 1, 1, 1, 1, 1, 1, 1, 1]
tail = ['','','','','的']

carbrand = readexcel(0, '/home/yzs/Downloads/data_require/carbrand.xlsx')

def car_choose(index):
    '''读取excel文件'''
    brand = readexcel(index, '/home/yzs/Downloads/data_require/carbrand.xlsx')
    return brand

series = car_choose(1)#系列
# print(len(series))
abbreviation = car_choose(2)#车辆品牌的简称

def choicepcc():
    '''选出进口车和非进口车，要让非进口车比例少一点'''
    pro_city_county_main = []
    pro_city_county_other = []
    i=0
    for e in carbrand:
        if e[0:2] in ['进口']:
            pro_city_county_main.append(i)
        else:
            pro_city_county_other.append(i)
        i = i + 1
    return pro_city_county_other,pro_city_county_main

class CarBrand:
    '''主要用到这个类的choose函数，就是从list中选取一个，即为choice(list)'''
    def __init__(self):
        self.items_list = str()
        self.items_choice = str()

    def update(self, iterable):
        self.items_list = ''.join(iterable)
        return self.items_list

    def choose(self, iterable, weight,flag = True):
        if flag:
                self.items_choice =choice(iterable)
                # print('o')
        else:
                weight_choose = windex(weight)
                choose = iterable[weight_choose]
                self.items_choice = choose
        return self.items_choice



if __name__ =="__main__":
    home,inlet=choicepcc()
    num_data = 4500
    C = CarBrand()
    carbrand_data = list()
    #国产车全称全匹配
    for i in range(num_data):
        home_c ,home_w= sample(home,2)
        # print(home_c)
        inlet_c = choice(inlet)
        b1 = carbrand[home_c]#全称
        b22 = series[home_w]#错的系列
        b2 = series[home_c]#对的系列
        ca = abbreviation[home_c]#简称
        a1 = carbrand[home_w]
        a2 = abbreviation[home_w]
        if isinstance(b2, float):
            b2=str(int(b2))
        if isinstance(b22, float):
            b22=str(int(b22))
        car_total = b1 + b2
        # print(car_total)
        a=C.choose(head,weight_head,flag=False)
        c=C.choose(tail,weight_head)
        # d=C.update([a,ca+b2,c])
        # d=C.update([a,ca+b22,c])
        # d=C.update([a,b1+b2,c])
        d=C.update([a,ca+b2,c])
    #     # print(d,b1,b2)
        carbrand_dict = dict()
        carbrand_dict['label_name'] = 'carbrand'
        carbrand_dict['id'] = i
        carbrand_dict['ref'] = d
        carbrand_dict['write'] = car_total
        carbrand_dict['m_brand'], carbrand_dict['m_series'] = 1,1
        carbrand_dict['brand_w'], carbrand_dict['series_w'] = b1,b2
        carbrand_data.append(carbrand_dict)
    # print(carbrand_data)
    obj = json.dumps(carbrand_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/gendata/daqige/carbrand_20000/carbrand_simple_homeseriesno_gen_0611_'+str(num_data)+'.json', 'w')
    file.write(obj)
    file.close()

    # #进口车
    # for i in range(num_data):
    #     home_c ,home_w= sample(inlet,2)
    #     # print(home_c)
    #     # inlet_c = choice(inlet)
    #     b1 = carbrand[home_c]#全称
    #     b22 = series[home_w]#错的系列
    #     b2 = series[home_c]#对的系列
    #     ca = abbreviation[home_c]#简称
    #     a1 = carbrand[home_w]
    #     a2 = abbreviation[home_w]
    #     if isinstance(b2, float):
    #         b2=str(int(b2))
    #     if isinstance(b22, float):
    #         b22=str(int(b22))
    #     car_total = b1 + b2
    #     # print(car_total)
    #     a=C.choose(head,weight_head,flag=False)
    #     c=C.choose(tail,weight_head)
    #     # d=C.update([a,ca+b2,c])
    #     # d=C.update([a,ca+b22,c])
    #     d=C.update([a,b1,c])
    # #     # print(d,b1,b2)
    #     carbrand_dict = dict()
    #     carbrand_dict['label_name'] = 'carbrand'
    #     carbrand_dict['id'] = i
    #     carbrand_dict['ref'] = d
    #     carbrand_dict['write'] = car_total
    #     carbrand_dict['m_brand'], carbrand_dict['m_series'] = 1,2
    #     carbrand_dict['brand_w'], carbrand_dict['series_w'] = b1,b2
    #     carbrand_data.append(carbrand_dict)
    # print(carbrand_data)
    obj = json.dumps(carbrand_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/gendata/daqige/carbrand_20000/inlet_gen_0611_'+str(num_data)+'_3.json', 'w')
    file.write(obj)
    file.close()

