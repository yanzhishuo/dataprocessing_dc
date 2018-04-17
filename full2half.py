# -*- coding:utf-8 -*-
#####-----------------早期的版本,含有程序 取json文件的键值--------------
import json

def DBC2SBC(ustring):
    rstring =""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 0x3000:
            inside_code = 0x0020
        else:
            inside_code -= 0xfee0
        if not (0x0021 <= inside_code and inside_code <= 0x7e):
            rstring += uchar
            continue
        rstring += chr(inside_code)
    return rstring

if __name__ == '__main__':
    with open('/home/yzs/workspace/dataprocessing/2018-04-08/phonenumber_with_id.json') as f:
        data = json.load(f)
    keys = ['write','write_han','ref','id']
    data_output = list()
    #直接替换,不用key循环
    for item in data:
        d=dict()
        if item['asr'] =='':
            continue
        else:
            for key in keys:
                d[key] = item[key]
            d['asr'] = DBC2SBC(item['asr'])
            #print(d)
            data_output.append(d)
    print(data_output)
    obj=json.dumps(data_output, ensure_ascii=False, indent=2)
    file=open('/home/yzs/workspace/yzs0408/phonenumber_with_id.json','w')
    print(type(obj))#dumps是将dict/list转化成str格式
    file.write(obj)
    file.close()

