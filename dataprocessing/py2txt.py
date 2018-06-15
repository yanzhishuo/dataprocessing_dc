import json
import pathlib
from datetime import datetime

def datenow():
    '''output：今天的日期（月日）如0521'''
    daten = datetime.now().strftime('%m%d')
    return daten
p = pathlib.Path('.')

for file in p.glob('*/*.json'):
    with open(str(file)) as f:
        data=json.load(f)
    data_output=list()
    keys ='ref'
    for item in data:
        d=dict()
        # for key in keys:
        d['ref']=item['ref']
        data_output.append(d['ref'])
    # print(data_output)
    print(type(data_output))
    with open('/home/yzs/gendata/data_all/txt' + str(file)[:5] + '_gen_' + str(datenow()) + '.txt', "w") as f:
        for num,i in enumerate(data_output):
            f.write(str(num + 1)+':'+i+'\n')