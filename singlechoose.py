import json
from weight_choice import *
from random import *

head = ['', '恩', '我看看', '我不确定']
demonstrative = ['', '这个问题', '这一题', '这题', '这个']
clientch = ['', '我选', '选', '我选的是', '我的选择是','是']
letter_con = ['一', '二', '三', '四', '五','第一个','第二个','第三个','第四个','第五个','第一','第二','第三','第四','第五',]
modal = ['', '吧', '啊', '呀']

def singlechoose_type():
    singlechoose_client = choice(letter_con)
    singlechoose_raw = head[windex([3,1,1,1])] + demonstrative[windex([4,1,1,1,1])] + clientch[windex([3,1,1,1,1,1,])]+singlechoose_client+ modal[windex([4,1,1,1])]
    return singlechoose_raw, singlechoose_client


if __name__ =="__main__":
    num_data = 2000
    # num_data = 2
    singlechoose_data = list()
    for i in range(num_data):
        singlechoose_dict = dict()
        singlechoose_dict['label_name'] = 'singlechoose'
        singlechoose_dict['id'] = i
        singlechoose_dict['ref'],singlechoose_dict['write']  = singlechoose_type()
        singlechoose_data.append(singlechoose_dict)
    # print(singlechoose_data)
    obj = json.dumps(singlechoose_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/singlechoose_gen_0508_2000.json', 'w')
    file.write(obj)
    file.close()