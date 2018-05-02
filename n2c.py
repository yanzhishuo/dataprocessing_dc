"""
n2c

"""
import re
from collections import namedtuple

from num2chinese import num2chinese


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
    if content[0] == '-':
        return '负' + n2c(content[1:])  # + '倍'
    return n2c(content)


def full_n2c(sentence):
    """Convert all number to chinese in sentence.

    Args:
        sentence:

    Returns:

    """
    Pattern = namedtuple('Pattern', ['programs', 'callback']) # pylint: disable=invalid-name
    patterns = [
        Pattern(re.compile(r'\d{1,2}[:：]\d{1,2}'), re_time_callback),
        Pattern(re.compile(r'\d{1,3}(?=(月|日|号|单元|岁|幢|户|室))'), re_ns_callback),
        # Pattern(re.compile(r'-?\d{1,3}(?=倍)'), re_minus_callback),
        # Pattern(re.compile(r'-?\d{1,3}(?=倍)'),  re_ns_callback),
        Pattern(re.compile(r'\d+'), re_sp_callback),
    ]
    for pattern in patterns:
        sentence = pattern.programs.sub(pattern.callback, sentence)
    return sentence


if __name__ == "__main__":
    TEST_SENTENCE = "2017年12月13日东苑大厦13号12:44给我4,-7倍数1454的47倍"
    TEST_SENTENCE1 = "27岁"
    print(full_n2c(TEST_SENTENCE))

