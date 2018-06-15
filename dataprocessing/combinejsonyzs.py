import pathlib
import json
from gendata.inherit import *
### 该代码是把当前路径下的json文件都合在一起
path = 'test_color'
p = '/home/yzs/gendata'
data_path = pathlib.Path(p)
data_combine = []
i= 0
for json_path in data_path.glob('*.json'):
    print(json_path)
    with open(str(json_path)) as f:
        data = json.load(f)
    for item in data:
        item['id']= i
        i = i+1
        data_combine.append(item)
obj = json.dumps(data_combine, ensure_ascii=False, indent=2)
file = open(p +'/'+path+'_gen_'+str(datenow())+'.json', 'w')
file.write(obj)
file.close()