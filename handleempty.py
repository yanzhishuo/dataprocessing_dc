import json
from extractasr1 import full_n2c #数字转中文

def handleempty(filename,path):
    with open(filename) as fp:
        data = json.load(fp)
    data_output = list()
    i =0
    for item in data:
         if item['asr'] =='':
             continue
         item['asr'] = full_n2c(item['asr'])
         item['id'] = i
         i = i+1
         data_output.append(item)
    obj=json.dumps(data_output,ensure_ascii=False,indent=2)
    file = open(path, 'w')
    file.write(obj)
    file.close()

if __name__ =="__main__":
    filename = '/home/yzs/workspace/dataprocessing/age_year_gen_0502_2000.json'
    handleempty(filename,'age.json')
