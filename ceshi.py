import string
import sys

def del_punc(text):
    punctuation = string.punctuation
    punctuation += '。？！，、；：“”﹃﹄「」﹁﹂（）—［］〔〕【】…－-～·‧《》〈〉﹏＿. '
    punctuation = set(punctuation)
    for i in ':：':
        punctuation.remove(i)
    return ''.join([i for i in text.strip() if i not in punctuation])

if __name__ == '__main__':
    print(del_punc('ew3,41!'))
