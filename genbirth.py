#需要1958-2000
from faker import Faker
import json
from random import *
from weight_choice import *

for j in range(10):
    fake = Faker(locale='zh_CN')
    data_raw = fake.date_between(start_date='-60y', end_date='-18y')
    data_str = data_raw.strftime('%Y-%m-%d')#datetime.date怎么转换为string
    year_raw, month_raw, day_raw = data_str.split('-')
    month_nozero = str(int(month_raw))
    day_nozero = str(int(day_raw))

    year_use = [year_raw, year_raw[2:]]
    month_use = [month_raw, month_nozero]
    day_use = [day_raw, day_nozero]


    title_pattern = ['','我']
    year_pattern = ['', '年']
    month_pattern = ['', '月']
    day_pattern = ['', '日', '号']
    Modal = ['', '啊', '的']

    num_data = 10

    for i in range(num_data):
        month_choice = choice(month_use)
        if month_choice == month_use[0]:
            gen_pattern = choice(title_pattern) + choice(year_use) + choice(year_pattern) + month_choice + day_raw + choice(Modal)
        else:
            gen_pattern = choice(title_pattern) + choice(year_use) + choice(year_pattern) + choice(Modal) + choice(month_use)  \
                  + choice(month_pattern)  + choice(day_use) + choice(day_pattern) + choice(Modal)
        print(gen_pattern)




# filename = open('birthday0422.json','w')
# data = []
#     asr, ref, write, label = get_birthday(fake)
#     dic = {}
#     dic['ref'] = ref
#     dic['write'] = write
#    # dic['label'] = label
#     dic['label_name'] = 'birthday'
#     data.append(dic)
# data = json.dumps(data,ensure_ascii=False,indent=2)
# filename.write(data)
