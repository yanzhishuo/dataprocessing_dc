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
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 变动代码位置需改这里
from models import Data

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

class BaseHandleDBD:

    def __init__(self,
                 db_path,
                 save_dir='/hd4T/dialog_data_stage_2_variation/4_census_m/stage_2_limit/asr'
                 ):
        """连接数据库

            Note:
                self.save = Path('/hd4T/yanghongkai/wulumuqi/db2json')
        """
        _engine = 'sqlite:///{}'.format(db_path)
        engine = create_engine(_engine)
        _session = sessionmaker()
        _session.configure(bind=engine)
        self.session = _session()
        self.save_dir = pathlib.Path(save_dir).joinpath(datetime.now().strftime('%Y-%m-%d'))

    def queryasr(self):
        query = self.session.query(Data)
        json_file_stem = list()
        for user in query:
            if user.json_file_stem not in json_file_stem:
                json_file_stem.append(user.json_file_stem)
        for item in json_file_stem:
                json_list_db = []
                raw_db =query.filter(Data.json_file_stem == item).order_by(Data.id).all()
                for data in raw_db:
                    _dict = dict()
                    _dict['asr'] = data.asr
                    if _dict['asr'] !='':
                            json_list_db.append(_dict['asr'])
                print(item,len(json_list_db))

    def load_data_from_db(self,
                          json_file):
        json_file = pathlib.Path(json_file)
        json_file_stem = json_file.stem
        json_file_name = json_file.name
        # 以文件名(不带拓展为依据)读数据
        json_list_db = []
        raw_db = self.session.query(Data).filter(
            Data.json_file_stem == json_file_stem).order_by(Data.id).all()
        for data in raw_db:
            _dict = dict()
            _dict['asr'] = data.asr
            if _dict['asr'] !='':
                json_list_db.append(_dict['asr'])
        save_dir = self.save_dir
        print(len(json_list_db))
        # for i, line in enumerate(json_list_db):
        #     stem = 'case{:05d}'.format(i)
        #     save_dir.mkdir(parents=True, exist_ok=True)
        #     sub_folder = save_dir.joinpath(stem)
        #     sub_folder.mkdir(mode=0o775)
        #     file_path =sub_folder.joinpath(stem)
        #     with file_path.open('w') as fp_o:
        #         fp_o.write(line)
        return json_list_db, save_dir

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', type=str, help='which db you want to bind')
    parser.add_argument('--json', type=str, help='which json you want to merge')
    args = parser.parse_args()
    for json_file,  db_path in[
        ('/hd4T/yanghongkai/recorder_server_data/expand_census_0502_8_20000/census_pcc_gen_0502_3000.json',
         '/hd4T/yanghongkai/recorder_server_data/expand_census_0502_8_20000/db.sqlite'),
    ]:
        handle = BaseHandleDBD(db_path=db_path)
        a, save_dir = handle.load_data_from_db(json_file)
        print(save_dir)
        # ---------------数字转中文
        dataChinese = list()
        for item in a:
            dataChinese.append(full_n2c(item))
        # --------------标点
        datafilter = list()
        for item in dataChinese:
            datafilter.append(del_punc(item))

        ###----全角转半角加上大写
        databc = list()
        for item in datafilter:
            item.upper()
            databc.append(DBC2SBC(item))

        for i, line in enumerate(databc):
            stem = 'case{:05d}'.format(i)
            save_dir.mkdir(parents=True, exist_ok=True)
            sub_folder = save_dir.joinpath(stem)
            sub_folder.mkdir(mode=0o775)
            file_path =sub_folder.joinpath(stem)
            with file_path.open('w') as fp_o:
                fp_o.write(line)
        handle.queryasr()
