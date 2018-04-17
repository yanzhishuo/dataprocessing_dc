#!/usr/bin/env python3

"""
How to use:

cat <data_file> | ./main.py > <out_file>

"""

import pathlib
import string
import sys

# punctuation = string.punctuation#英文标点
#
# punctuation += '。？！，、；：“”﹃﹄「」﹁﹂（）—［］〔〕【】…－-～·‧《》〈〉﹏＿. '
# punctuation = set(punctuation)
# for i in ':：':
#     punctuation.remove(i)


def del_punc(text):
    punctuation = string.punctuation

    punctuation += '。？！，、；：“”﹃﹄「」﹁﹂（）—［］〔〕【】…－-～·‧《》〈〉﹏＿. '
    punctuation = set(punctuation)
    for i in ':：':
        punctuation.remove(i)###标点保留：是吗
    return ''.join([i for i in text.strip() if i not in punctuation])


if __name__ == '__main__':
    for line in sys.stdin:
        print(''.join([i for i in line.strip() if i not in punctuation]))
