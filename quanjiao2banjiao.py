# -*- coding:utf-8 -*-
###-------------asr的全角转半角 及删除asr为空的程序以这份为主
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
    with open('/home/yzs/workspace/dataprocessing/2018-04-09/name_with_id.json') as f:
        data = json.load(f)
    data_output = list()
    for item in data:
        #item.pop('asr')
        item['asr'] = DBC2SBC(item['asr'])
        if item['asr'] =='':
            continue
        data_output.append(item)
    print(data_output)
    obj=json.dumps(data_output,ensure_ascii=False,indent=2)
    file=open('/home/yzs/workspace/yzs0409/name_with_id.json','w')
    print(type(obj))#dumps是将dict/list转化成str格式
    file.write(obj)
    file.close()

