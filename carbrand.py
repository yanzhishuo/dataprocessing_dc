from random import *
import json
from weight_choice import *
from genpassword import *
from pyexcel import *
from genpassword import *

vehiclebrand = readexcel(0, '/home/yzs/Downloads/data_require/carbrand.xlsx')
# print(vehiclebrand)
vehicle_series = readexcel(1, '/home/yzs/Downloads/data_require/carbrand.xlsx')
# carbrands = readexcel(2, '/home/yzs/Downloads/data_require/carbrand.xlsx')
# carbrand = readexcel(3, '/home/yzs/Downloads/data_require/carbrand.xlsx')
# brand_series = readexcel(4, '/home/yzs/Downloads/data_require/carbrand.xlsx')
head = ['','那个','我的是','我的车是','我的车辆品牌是','我的车品牌是','车牌子是','是','品牌是','牌子是']
# print([1]*len(head))
weight_head = [3, 2, 1, 1, 1, 1, 1, 1, 1, 1]
tail = ['','的']

def car_choose(index):
    brand = readexcel(index, '/home/yzs/Downloads/data_require/carbrand.xlsx')
    return brand

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



if __name__ =="__main__":
    num_data = 3000
    C = CarBrand()
    carbrand_data = list()
    for i in range(num_data):
        a=C.choose(head,weight_head,flag=False)
        num_c = gennum(0,len(vehiclebrand)-1)
        print(num_c)
        b1 = vehiclebrand[num_c]
        b2 = vehicle_series[num_c]
        if isinstance(b2,float):
            b2=str(int(b2))
        b = b1+b2
        c=C.choose(tail,weight_head)
        d=C.update([a,b,c])
        # print(d,b1,b2)
        carbrand_dict = dict()
        carbrand_dict['label_name'] = 'carbrand'
        carbrand_dict['id'] = i
        carbrand_dict['ref'] = d
        carbrand_dict['write'] = b
        carbrand_dict['brand_m'], carbrand_dict['series_m'] = 1,1
        carbrand_dict['brand_w'], carbrand_dict['series_w'] = b1,b2
        carbrand_data.append(carbrand_dict)
    # print(carbrand_data)
    obj = json.dumps(carbrand_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/carbrand_series_gen_0509_3000.json', 'w')
    file.write(obj)
    file.close()

