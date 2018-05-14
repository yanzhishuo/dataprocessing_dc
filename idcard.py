from random import *
from faker import Faker
import re
import json
from weight_choice import *
from genpassword import *
from pyexcel import *


idcardsix = readexcel(0, '/home/yzs/Downloads/idcard6.xlsx')
print(len(idcardsix))
fake = Faker(locale='zh_CN')
def genidcard():
    data_raw = fake.date_between(start_date='-65y', end_date='-18y')
    data_str = data_raw.strftime('%Y-%m-%d')  # datetime.date怎么转换为string
    year_raw, month_raw, day_raw = data_str.split('-')
    middle8 = year_raw+month_raw+day_raw
    shunxuma = gennumpassword(3)
    last_list = [0,1,2,3,4,5,6,7,8,9,'X']
    last = choice(last_list)
    # print(type(str(choice(idcardsix))),type(middle8),type(shunxuma))
    idcard_raw = str(int(choice(idcardsix))) + middle8 +shunxuma+str(last)
    return idcard_raw

if __name__ =="__main__":
    num_data = 3500
    idcard_data = list()
    for i in range(num_data):
        idcard_dict = dict()
        idcard_dict['label_name'] = 'idcard'
        idcard_dict['id'] = i
        idcard_dict['ref'] = genidcard()
        idcard_data.append(idcard_dict)
    # print(idcard_data)
    obj = json.dumps(idcard_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/idcard_gen_0508_3500.json', 'w')
    file.write(obj)
    file.close()