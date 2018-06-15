import json
import pathlib

p = '/home/yzs/workspace/dataprocessing/dataprocessing'
data_path = pathlib.Path(p)
json_path = data_path.joinpath('chuan.json')
with open(str(json_path)) as f:
    data = json.load(f)
data_global = []
for item in data:
    item['global_id'] = str(json_path).split('/')[-1]
    data_global.append(item)
obj=json.dumps(data_global, ensure_ascii=False, indent=2)
file=open(str(json_path),'w')
file.write(obj)
file.close()