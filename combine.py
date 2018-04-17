import json

if __name__ == '__main__':
    with open('/home/yzs/workspace/dataprocessing/20180415/birthday_with_id.json') as f:
        data = json.load(f)
    with open('/home/yzs/workspace/dataprocessing/DialogProject-parse-0411-500/birthday.json') as f1:
        data1 = json.load(f1)
    for item in data:
        data1.append(item)
    print(data1)
    obj=json.dumps(data1,ensure_ascii=False,indent=2)
    file=open('/home/yzs/workspace/yzs0415/birthday_with_id.json','w')
    print(type(obj))#dumps是将dict/list转化成str格式
    file.write(obj)
    file.close()