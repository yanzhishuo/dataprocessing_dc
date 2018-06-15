from random import *
import json
from weight_choice import *
from genpassword import *
from pyexcel import *
from genpassword import *

labeldict = {'匹配':1,'':2,'错误匹配':0}
vehiclebrand = readexcel(0, '/home/yzs/Downloads/data_require/carbrand.xlsx')
# print(vehiclebrand)
vehicle_series = readexcel(1, '/home/yzs/Downloads/data_require/carbrand.xlsx')
# carbrands = readexcel(2, '/home/yzs/Downloads/data_require/carbrand.xlsx')
# carbrand = readexcel(3, '/home/yzs/Downloads/data_require/carbrand.xlsx')
# brand_series = readexcel(4, '/home/yzs/Downloads/data_require/carbrand.xlsx')
head = ['','那个','我的车是','我的车辆品牌是','我的车品牌是','车牌子是','是','品牌是','牌子是']
# print([1]*len(head))
weight_head = [3, 1, 1, 1, 1, 1, 1, 1, 1]
tail = ['','的']

def car_choose(index):
    brand = readexcel(index, '/home/yzs/Downloads/data_require/carbrand.xlsx')
    return brand

brand_soft = car_choose(2)

class CarBrand:
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
                # print(iterable)
                # print(item)
                weight_choose = windex(weight)
                # print(weight_choose)
                choose = iterable[weight_choose]
                # print(choose)
                self.items_choice = choose
        return self.items_choice

def float2str(b2):
    if isinstance(b2, float):
        b2 = str(int(b2))
    else:
        b2 = b2
    return b2

def carbrand_choose(list_input,list_except):
    list_choice = list()
    for e in list_input:
        if e not in list_except:
            list_choice.append(e)
    carbrand = choice(list_choice)
    return carbrand


if __name__ =="__main__":
    num_data = 2472
    C = CarBrand()
    carbrand_data = list()
    for i in range(num_data):
        a=C.choose(head,weight_head,flag=False)
        b1 = vehiclebrand[i]
        b2_r = float2str(vehicle_series[i])
        series_list = [choice(vehicle_series[:i]+vehicle_series[i+1:]),b2_r,'']
        # print(len(series_list))
        series_wrong = float2str(choice(series_list))
        if series_wrong == '':
            m_series = 2
        elif series_wrong == b2_r:
                m_series = 1
        else:
                m_series = 0
        b = b1+b2_r
        print(i)
        # carbrand_r = choice([brand_soft[i],vehiclebrand[i]])
        carbrand_wrong = carbrand_choose(list(set(vehiclebrand)),[brand_soft[i],vehiclebrand[i]])
        print(carbrand_wrong,series_wrong)
        bs = carbrand_wrong + series_wrong
        # d=C.update([a,b2])
        d=C.update([a,bs])
        carbrand_dict = dict()
        carbrand_dict['label_name'] = 'carbrand'
        carbrand_dict['id'] = i
        carbrand_dict['ref'] = d
        carbrand_dict['write'] = b
        carbrand_dict['m_brand'], carbrand_dict['m_series'] = 0,m_series
        carbrand_dict['brand_w'], carbrand_dict['series_w'] = b1,b2_r
        carbrand_data.append(carbrand_dict)
    # print(carbrand_data)
    obj = json.dumps(carbrand_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/carbrand_wrong/carbrandwrong_series_gen_0514_'+str(num_data)+'.json', 'w')
    file.write(obj)
    file.close()

