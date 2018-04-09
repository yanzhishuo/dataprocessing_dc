'''
1.jason的asr转文件
2.去标点
3.数字转中文
'''

#!/usr/bin/env python3
import argparse
import os
import pathlib
import json
import string
import sys
import re
from collections import namedtuple

from num2chinese import num2chinese


def del_punc(text):
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

    Args:
        sentence:

    Returns:

    """
    Pattern = namedtuple('Pattern', ['programs', 'callback']) # pylint: disable=invalid-name
    patterns = [
        Pattern(re.compile(r'\d{1,2}[:：]\d{1,2}'), re_time_callback),
        Pattern(re.compile(r'\d{1,3}(?=(月|日|号|单元))'), re_ns_callback),
        Pattern(re.compile(r'-\d{1,2}(?=倍)'), re_minus_callback),
        Pattern(re.compile(r'\d+'), re_sp_callback),
    ]
    for pattern in patterns:
        sentence = pattern.programs.sub(pattern.callback, sentence)
    return sentence


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('in_path', type=str)
    parser.add_argument('--label_d', type=int)
    parser.add_argument('--case', type=int)
    args = parser.parse_args()
    if args.label_d is None:
        args.label_d = 0
    if args.case is None:
        args.case = 0
    if args.label_d > 999:
        raise ValueError
    folder = pathlib.Path('label_d{:03d}'.format(args.label_d))
    if not folder.exists():
        folder.mkdir(mode=0o775)
    in_path = pathlib.Path(args.in_path)
    with in_path.open('r') as fp:
        data=json.load(fp)
    ####-----------提取出asr对应的句子
    dataitem=list()
    for item in data:
        if item['asr'] == '':
            continue
        dataitem.append(item['asr'])

    # ---------------数字转中文
    dataChinese = list()
    for item in dataitem:
        dataChinese.append(full_n2c(item))
    #--------------标点
    datafilter=list()
    for item in dataChinese:
        datafilter.append(del_punc(item))

    #print(dataChinese)
    for i, line in enumerate(datafilter):
            stem = 'case{:05d}'.format(i)
            sub_folder = folder.joinpath(stem)
            sub_folder.mkdir(mode=0o775)
            file_path = sub_folder.joinpath(stem)
            with file_path.open('w') as fp_o:
                fp_o.write(line)
