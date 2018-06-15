import random
import json
from gendata.inherit import *

with open('/home/yzs/gendata/test_color_gen_0615_8062.json') as f:
    data = json.load(f)
shuffle(data)
print(data)
print(len(data))
def Interceptionsection(num,path2,number):
    for i in range(num):
        data_output = list()
        for j,item in enumerate(data):
            print(i)
            if j in range(number*i,number*(i+1)):
                item["id"] = j
                data_output.append(item)
        print(len(data_output))
        obj=json.dumps(data_output,ensure_ascii=False,indent=2)
        file=open('/home/yzs/gendata/'+path2+'_gen_'+str(datenow())+'_'+str(number)+'_'+str(i+1)+'.json','w')
        file.write(obj)
        file.close()

if __name__ == '__main__':
    Interceptionsection(5,'test_color',100)