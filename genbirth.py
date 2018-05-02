#需要1958-2000
from faker import Faker
import json
from random import *
from weight_choice import *
import time

start = time.clock()

year_pattern = ['', '年']
month_pattern = ['', '月']
attribute = ['', '的']
day_pattern = ['', '日', '号']

def date_ymd():
    fake = Faker(locale='zh_CN')
    data_raw = fake.date_between(start_date='-60y', end_date='-18y')
    data_str = data_raw.strftime('%Y-%m-%d')  # datetime.date怎么转换为string
    year_raw, month_raw, day_raw = data_str.split('-')
    month_nozero = str(int(month_raw))
    day_nozero = str(int(day_raw))
    year_use = [year_raw, year_raw[2:]]
    month_use = [month_raw, month_nozero, '']
    day_use = [day_raw, day_nozero, '']
    month_choice = month_use[windex([1,5,4])]
    if month_choice == '':
        gen_pattern = choice(year_use) + '年' +attribute[windex([9.9, 0.1])]
    elif month_choice[0] == '0':
        gen_pattern = choice(year_use) + choice(year_pattern) +attribute[windex([9.9, 0.1])] + month_choice + day_raw
    else:
        month_patternc = choice(month_pattern)
        if month_patternc == '' and len(month_choice) != 1:
            gen_pattern = choice(year_use) + choice(year_pattern) +attribute[windex([9.9, 0.1])] + month_choice  + choice(day_use)
        else:
            day_choice = choice([day_nozero,''])
            if day_choice == '':
                gen_pattern = choice(year_use) + choice(year_pattern) +attribute[windex([9.9, 0.1])] + month_choice + '月'
            else:
                gen_pattern = choice(year_use) + choice(year_pattern)+attribute[windex([9.9, 0.1])] + month_choice + '月'+day_choice+choice(day_pattern)
    return gen_pattern

def date_yearmd():
    fake = Faker(locale='zh_CN')
    data_raw = fake.date_between(start_date='-60y', end_date='-18y')
    data_str = data_raw.strftime('%Y-%m-%d')  # datetime.date怎么转换为string
    year_raw, month_raw, day_raw = data_str.split('-')
    month_nozero = str(int(month_raw))
    day_nozero = str(int(day_raw))
    year_use = [year_raw, year_raw[2:]]
    month_use = [month_raw, month_nozero, '']
    day_use = [day_raw, day_nozero, '']
    month_choice = month_use[windex([1,5,4])]
    if month_choice == '':
        gen_pattern = choice(year_use) + '年' +attribute[windex([9.9, 0.1])]
    elif month_choice[0] == '0':
        gen_pattern = choice(year_use) + '年'+attribute[windex([9.9, 0.1])] + month_choice + day_raw
    else:
        month_patternc = choice(month_pattern)
        if month_patternc == '' and len(month_choice) != 1:
            gen_pattern = choice(year_use) + '年'+attribute[windex([9.9, 0.1])] + month_choice  + choice(day_use)
        else:
            day_choice = choice([day_nozero,''])
            if day_choice == '':
                gen_pattern = choice(year_use) + '年'+attribute[windex([9.9, 0.1])] + month_choice + '月'
            else:
                gen_pattern = choice(year_use) + '年'+attribute[windex([9.9, 0.1])] + month_choice + '月'+day_choice+choice(day_pattern)
    return gen_pattern

Modal = ['啊', '']
#type1
title_pattern = ['我', '我是', '']
born_pattern = ['出生在', '生在', '出生于', '']
#type2
born_pattern1 = ['出生', '生的', '出生的', '']
#type3
title_pattern1 = ['我', '我的']
born_pattern2 = ['生日是', '身份证上是', '出生年月日是']


def birth_t1():
    ymd = date_ymd()
    birth_raw1 = title_pattern[windex([3,1,5])]+choice(born_pattern)+ ymd +Modal[windex([1,9])]
    return birth_raw1, ymd

def birth_t2():
    ymd = date_ymd()
    birth_raw2 = title_pattern[windex([3,1,5])]+ymd+choice(born_pattern1)+Modal[windex([0.1,9.9])]
    return birth_raw2, ymd

def birth_t3():
    ymd = date_ymd()
    birth_raw3 = title_pattern1[windex([4,6])]+choice(born_pattern2)+ymd+Modal[windex([0.1,9.9])]
    return birth_raw3, ymd

def gen_birth():
    birth_list = [birth_t1(), birth_t2(), birth_t3()]
    birth_ref,birth_write = choice(birth_list)
    return birth_ref,birth_write

if __name__ == "__main__":
    num_data = 5000
    list_data = list()
    label_name = 'birthday'
    for i in range(num_data):
        list_dict = dict()
        list_dict['label_name'] = label_name
        list_dict['id'] = i
        list_dict['ref'], list_dict['write'] = gen_birth()
        list_data.append(list_dict)
    obj = json.dumps(list_data, ensure_ascii=False, indent=2)
    file = open('/home/yzs/' + label_name + '_gen_0424_'+str(num_data)+'.json', 'w')
    file.write(obj)
    file.close()
    end = time.clock()
    print('Running time:%s seconds'%(end - start))

