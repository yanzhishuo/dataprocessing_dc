import json
with open('/home/yzs/json/data0/address_with_id.json') as f:
    data=json.load(f)
print(type(data))
print(data[0])
print(type(data[0]))
data_output=list()
keys=['asr','ref','id']
for item in data:
    d=dict()
    for key in keys:
        d[key]=item[key]
        data_output.append(d)
print(data_output)
print(type(data_output))
obj=json.dumps(data_output,ensure_ascii=False,indent=2)
file=open('/home/yzs/yzs.json','w')
print(type(obj))#dumps是将dict/list转化成str格式
file.write(obj)
file.close()
