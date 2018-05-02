import json

if __name__ == '__main__':
    path = '/home/yzs/name_gen_0425_10000.json'
    with open(path) as f:
        data = json.load(f)
    for i in range(5):
        data_output = list()
        for item in data:
            print(i)
            if item['id'] in range(2000*i,2000*(i+1)):
                data_output.append(item)
        print(data_output)
        obj=json.dumps(data_output,ensure_ascii=False,indent=2)
        file=open('/home/yzs/name_gen_0425_10000_'+str(i+1)+'.json','w')
        print(type(obj))#dumps是将dict/list转化成str格式
        file.write(obj)
        file.close()