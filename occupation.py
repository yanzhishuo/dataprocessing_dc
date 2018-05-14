import json
from random import *
from weight_choice import *

head = ['','我', '我是','我现在','我目前', '我的职业身份是','我的职业是']
opt = ['自己做生意','在职人员','待业']
modal = ['','了','啊','呀']

def opt_type():
    opt_c = choice(opt)
    opt_raw = choice(head) +opt_c + modal[windex([5,1,1,1])]
    return opt_raw, opt_c

if __name__ =="__main__":
    num_data = 1000
    # num_data = 2
    occupation_data = list()
    for i in range(num_data):
        occupation_dict = dict()
        occupation_dict['label_name'] = 'occupation'
        occupation_dict['id'] = i
        occupation_dict['ref'],occupation_dict['write'] = opt_type()
        occupation_data.append(occupation_dict)
    # print(occupation_data)
    obj = json.dumps(occupation_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/occupation_gen_0508_1000.json', 'w')
    file.write(obj)
    file.close()
