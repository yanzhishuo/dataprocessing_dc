import json
from faker import Faker
from weight_choice import *
from random import *

head = ['','身份证','身份证的']
time_valid = ['','有效期','有效期是','有效期限是','有效期限']
attribute = ['','到']
# tail = ['','年']
tail = ['年']
fake = Faker(locale='zh_CN')
def genidcard():
    data_raw = fake.date_between(start_date='+0y',end_date='+20y')
    data_str = data_raw.strftime('%Y-%m-%d')  # datetime.date怎么转换为string
    year_raw, month_raw, day_raw = data_str.split('-')
    # print(year_raw)
    period = [year_raw[2:],'长期']
    # print(windex([2,1]))
    idvalid = period[windex([1,1.05])]
    # idvalid = choice(period)
    # print(idvalid)
    if idvalid == '长期':
        validperiod = choice(head) + choice(time_valid)+'长期'
    else:
        validperiod = choice(head) + choice(time_valid) + choice(attribute)+idvalid+choice(tail)
    return validperiod, idvalid

if __name__ =="__main__":
    num_data = 1000
    # num_data = 2
    idcard_data = list()
    for i in range(num_data):
        idcard_dict = dict()
        idcard_dict['label_name'] = 'validperiod'
        idcard_dict['id'] = i
        idcard_dict['ref'],idcard_dict['write'] = genidcard()
        idcard_data.append(idcard_dict)
    # print(idcard_data)
    obj = json.dumps(idcard_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/gendata/validperiod_gen_0605_1000.json', 'w')
    file.write(obj)
    file.close()
