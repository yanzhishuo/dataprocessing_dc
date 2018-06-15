import json
from random import *

head = ['','我的车是','我的车辆','我的车排量是','排放量是','我的车排放量']
em = ['0.6','0.8','1.0','1.1','1.2','1.3','1.4','1.5','1.6','1.7','1.8','1.9','2.0','2.2','2.3','2.4','2.5','2.7','2.8','3.0','3.2','3.4','3.5','3.6','3.8','4.0','4.2','4.3','4.4','4.6','4.8','5.0','5.2','5.4','5.6','5.8','6.0','6.2','6.4','6.8','7.0','7.2','7.8','8.0','8.2','12.2','16.4','18.8']
print(len(em))
tail = ['','升','T']

######下面这几行是为了给em即车辆排量权重
listVal = [1]*len(em)
listVal[5] = 5
listVal[8] = 10
listVal[10] = 10
listVal[12] = 8
listVal[20] = 3
listVal[36] = 2

def vehicleemission():
    emission = choice(em)
    print(emission)
    emission_raw = choice(head) + emission +choice(tail)
    return  emission_raw, emission


if __name__ =="__main__":
    num_data = 3000
    # num_data = 2
    emission_data = list()
    for i in range(num_data):
        emission_dict = dict()
        emission_dict['label_name'] = 'vehicleemission'
        emission_dict['id'] = i
        emission_dict['ref'],emission_dict['write'] = vehicleemission()
        emission_data.append(emission_dict)
    # print(emission_data)
    obj = json.dumps(emission_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/gendata/vehicleemission_gen_0615_'+str(num_data)+'.json', 'w')
    file.write(obj)
    file.close()