#该程序把所有的.V3文件改为.wav文件
import pathlib
import json
from subprocess import run
from datetime import datetime

def datenow():
    '''output：今天的日期（月日）如0521'''
    daten = datetime.now().strftime('%m%d')
    return daten

p = pathlib.Path('.')

# for file in p.glob('*/*.V3'):
# for file in p.glob('*/*/*.V3'):#当前目录下的两级子目录
j=0
for file in p.glob('*.json'):
    j=j+1
    print(type(file))
    with open('./'+str(file)) as f:
        data = json.load(f)
    num = 1
    number = 315
    path2 ='12_phone_color/color'
    print(j)
    for i in range(num):
        data_output = list()
        for item in data:
            # print(i)
            if item['id'] in range(number * i, number * (i + 1)):
                data_output.append(item)
        obj = json.dumps(data_output, ensure_ascii=False, indent=2)
        file = open('/home/yzs/gendata/' + path2 + '_gen_' + str(datenow()) + '_' + str(number) + '_' + str(j) + '.json', 'w')
        print(type(obj))  # dumps是将dict/list转化成str格式
        file.write(obj)
        file.close()

