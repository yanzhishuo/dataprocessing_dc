import json

with open('XJNER.json') as f:
    data=json.load(f)
print(type(data))
data_output=list()
keys=["part",'year','month','day']
keysyzs =['et','st','sloc','type']
for item in data:
    d=dict()
    for key in keys:
        if len(item[key])==1:
            d['s_'+key] = item[key][0]
            d['e_' + key] = ''
        elif len(item[key])==2:
            d['s_' + key] = item[key][0]
            d['e_' + key] = item[key][1]
        else:
            d['s_' + key] = ''
            d['e_' + key] = ''
    for key in keysyzs:
        if len(item[key])==1:
            d[key] = item[key][0]
        else:
            d[key] = ''
    d['ref'] = item['ref']
    d['asr'] = item['asr']
    d['id'] = item['id']
    print(d['id'])
    data_output.append(d)
print(data_output)
print(type(data_output))
obj=json.dumps(data_output, ensure_ascii=False, indent=2)
file=open('/home/yzs/XJ0605.json','w')
print(type(obj))#dumps是将dict/list转化成str格式
file.write(obj)
file.close()