import json

if __name__ == '__main__':
    with open('/home/yzs/workspace/dataprocessing/20180418/birthday.json') as f:
        data = json.load(f)
    with open('/home/yzs/workspace/dataprocessing/201804182/DialogProject_record_parse_0411_500/birthday.json') as f1:
        data1 = json.load(f1)
    for item in data:
        data1.append(item)
    print(data1)
    obj=json.dumps(data1,ensure_ascii=False,indent=2)
    file=open('/home/yzs/birthday.json','w')
    print(type(obj))#dumps是将dict/list转化成str格式
    file.write(obj)
    file.close()