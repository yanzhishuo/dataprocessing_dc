import argparse
from datetime import datetime
import json
import pathlib
import os
import string
import sys
import re
from collections import namedtuple

from num2chinese import num2chinese


def DBC2SBC(ustring):
    '''全角转半角'''
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

def del_punc(text):
    '''去标点'''
    punctuation = string.punctuation
    punctuation += '。？！，、；：“”﹃﹄「」﹁﹂（）—［］〔〕【】…－-～·‧《》〈〉﹏＿. '
    punctuation = set(punctuation)
    for i in ':：':
        punctuation.remove(i)
    return ''.join([i for i in text.strip() if i not in punctuation])

def n2c(num, sp=False):
    num_han = '零一二三四五六七八九'
    if sp:
        return ''.join([num_han[int(i)] for i in num])
    return num2chinese(num)


def re_sp_callback(match):
    return n2c(match.group(), sp=True)


def re_ns_callback(match):
    return n2c(match.group(), sp=False)


def re_time_callback(match):
    """time callback"""
    content = match.group()
    content = content.replace('：', ':')
    [hour, minute] = [n2c(i) for i in content.split(':')]
    if minute == '零':
        minute = ''
    else:
        minute += '分'
    return hour + '点' + minute


def re_minus_callback(match):
    """minus number callback"""
    content = match.group()
    print('min')
    return '负' + n2c(content[1:])  # + '倍'


def full_n2c(sentence):
    """Convert all number to chinese in sentence.
     数字转中文

    Args:
        sentence:

    Returns:

    """
    Pattern = namedtuple('Pattern', ['programs', 'callback']) # pylint: disable=invalid-name
    patterns = [
        Pattern(re.compile(r'\d{1,2}[:：]\d{1,2}'), re_time_callback),
        Pattern(re.compile(r'\d{1,3}(?=(月|日|号|单元))'), re_ns_callback),
        #Pattern(re.compile(r'-\d{1,2}(?=倍)'), re_minus_callback),
        Pattern(re.compile(r'\d+'), re_sp_callback),
    ]
    for pattern in patterns:
        sentence = pattern.programs.sub(pattern.callback, sentence)
    return sentence

if __name__ =='__main__':
   #看是否asr有重复
    with open('/home/yzs/confirm_gen_0513_10000.json') as f:
        data = json.load(f)
    data_output = list()

   #asr有没有重复
    # for item in data:
    #     # item.pop('asr')
    #     item['asr'] = full_n2c(item['asr'])
    #     if item['asr'] == '':
    #         continue
    #     # data_output.append(item)
    #     data_output.append(item['asr'])

#ref有没有重复
    for item in data:
        # item.pop('ref')
        item['ref'] = full_n2c(item['ref'])
        if item['ref'] == '':
            continue
        data_output.append(item)
    #     data_output.append(item['ref'])
    # print(len(data_output))
    # data_yzs = []
    # for e in data_output:
    #     if e not in data_yzs:
    #         data_yzs.append(e)
    #     else:
    #         print(e)
    # print(len(data_yzs))
    #
    l4 = []
    l4.append(data_output[0])
    # print(l4)
    for dict in data_output:
        k = 0
        # print(dict['asr'])
        for item in l4:
            # print(item['asr'])
            # if dict['asr'] != item['asr']:
            if dict['ref'] != item['ref']:
                k = k + 1
            else:
                break
            if k == len(l4):
                # print(k)
                l4.append(dict)
    print(len(l4))
    l=[]
    i=0
    for item in l4:
            item['id'] = i
            i = i +1
            l.append(item)
    print(len(l))

   # #     # data_output.append(item)
   #  # # print(data_output)
    obj = json.dumps(l, ensure_ascii=False, indent=2)
    file = open('/home/yzs/workspace/confirm_gen_0513_1337.json', 'w')
    print(type(obj))  # dumps是将dict/list转化成str格式
    file.write(obj)
    file.close()
   #  # obj = json.dumps(data_yzs, ensure_ascii=False, indent=2)
   #  # file = open('/home/yzs/workspace/vehicelemission2.json', 'w')
   #  # file.write(obj)
   #  # file.close()