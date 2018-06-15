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


if __name__ =="__main__":
    num_data = 2472
    C = CarBrand()
    carbrand_data = list()
    for i in range(num_data):
        a=C.choose(head,weight_head,flag=False)
        # num_c = gennum(0,len(vehiclebrand)-1)
        # print(num_c)
        # b1 = vehiclebrand[num_c]
        # b2 = vehicle_series[num_c]
        # b3 = brand_soft[num_c]
        # print(i)
        b1 = vehiclebrand[i]
        b2_r = float2str(vehicle_series[i])
        if i != 0:
            b2 = vehicle_series[i -1 ]
        else:
            b2 = '雷凌'
        if isinstance(b2,float):
            b2=str(int(b2))
        b = b1+b2_r
        # bs = b3+b2
        b22 = choice([brand_soft[i],vehiclebrand[i]])
        bs = b22 + b2
        # d=C.update([a,b2])
        d=C.update([a,bs])
        carbrand_dict = dict()
        carbrand_dict['label_name'] = 'carbrand'
        carbrand_dict['id'] = i
        carbrand_dict['ref'] = d
        carbrand_dict['write'] = b
        carbrand_dict['m_brand'], carbrand_dict['m_series'] = 1,0
        carbrand_dict['brand_w'], carbrand_dict['series_w'] = b1,b2_r
        carbrand_data.append(carbrand_dict)
    # print(carbrand_data)
    obj = json.dumps(carbrand_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/carbrand_wrong/carbrand_serieswrong_gen_0514_'+str(num_data)+'.json', 'w')
    file.write(obj)
    file.close()

