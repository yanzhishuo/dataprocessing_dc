import json
from random import *
from weight_choice import  *

labellist={'是':1,'否':2}

#label = 1
head = ['', '我看看', '稍等我看看']
status_ture = ['是', '是的','恩', '对', '恩对的','恩是的','恩是']
modal_true = ['', '啊', '哦','呀']

#label = 2
# head = ['', '我看看', '稍等我看看']
modal_no = ['', '啊', '额']
status_no = ['不是', '不是的']
address_past = ['', '我申请表写的是户口本地址','我申请表写的是身份证地址','我申请表写的是老家地址','我填的是身份证地址','我填的是老家地址','我填的是户口本地址','我申请表填的是身份证地址','我申请表填的是老家地址','我申请表填的是户口本地址']

#label = 2
# head = ['', '我看看', '稍等我看看']
# madal_no = ['', '啊', '额']
status_false = ['','不是', '不是的']
address_now= ['', '我现在租房子住','我暂时不住那里了','我现在没住在那里','我过一段时间回去住','我改了','我换地方了','我有时候住那','我一段时间住那','我大部分时间不在那里住','我现在在外地打工','我在别的地方工作','我换工作了就不住那里了','我马上搬家了','我不住那里了','我现在不住那里了']
modal_false = ['','啊','呀']

class Confirm(object):
    def __init__(self):
        self.items_list = str()
        self.items_choice = str()

    def update(self, iterable):
        self.items_list = ''.join(iterable)
        return self.items_list

    def choosesingle(self, iterable):
        self.items_choice =''.join(choice(iterable))
        return self.items_choice

    def choose(self, iterable):
        for item in iterable:
            self.items_choice = self.items_choice + choice(item)
        return self.items_choice


def confirm_yes():
    confirm = Confirm()
    label = 1
    confirm_true = confirm.choose([head,status_ture,modal_true])
    return confirm_true,label

def confirm_false():
    confirm = Confirm()
    label = 2
    confirm_no = confirm.choose([head,modal_no,status_false,address_now,modal_false])
    return confirm_no,label

def confirm_no():
    confirm = Confirm()
    label = 2
    confirm_no = confirm.choose([head,modal_no,status_no,address_past])
    return confirm_no,label

# print(confirm_yes())
# print(confirm_no())
# print(confirm_false())
def gen_confirm():
    confirm_list =[confirm_yes(), confirm_no(),  confirm_false()]
    confirm_ref, label_name = confirm_list[windex([1,2,2])]
    return confirm_ref, label_name

# print(len(address_past),len(address_now))

if __name__ == "__main__":
    num_data = 6000
    list_data = list()
    label_name = 'confirm'
    for i in range(num_data):
        list_dict = dict()
        list_dict['label_name'] = label_name
        list_dict['id'] = i
        list_dict['ref'], list_dict['label'] = gen_confirm()
        list_data.append(list_dict)
        print('loading')
    # print(list_data)
    obj = json.dumps(list_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/'+label_name+'_gen_0513_'+str(num_data)+'.json', 'w')
    file.write(obj)
    file.close()