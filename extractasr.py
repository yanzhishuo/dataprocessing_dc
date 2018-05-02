import argparse
from datetime import datetime
import json
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 变动代码位置需改这里
from models import Data

class BaseHandleDBD:

    def __init__(self,
                 db_path):
        """连接数据库

            Note:
                self.save = Path('/hd4T/yanghongkai/wulumuqi/db2json')
        """
        _engine = 'sqlite:///{}'.format(db_path)
        engine = create_engine(_engine)
        _session = sessionmaker()
        _session.configure(bind=engine)
        self.session = _session()

    def load_data_from_db(self,
                          json_file):
        json_file = pathlib.Path(json_file)
        json_file_stem = json_file.stem
        # json_file_name = json_file.name
        # 以文件名(不带拓展为依据)读数据
        json_list_db = []
        raw_db = self.session.query(Data).filter(
            Data.json_file_stem == json_file_stem).order_by(Data.id).all()
        for data in raw_db:
            _dict = dict()
            _dict['asr'] = data.asr
            json_list_db.append(_dict)
        return json_list_db

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', type=str, help='which db you want to bind')
    parser.add_argument('--json', type=str, help='which json you want to merge')
    args = parser.parse_args()
    for json_file, json_db_stem, db_path in[
        ('/hd4T/yanghongkai/recorder_server_data/dc_recorder/phonenumber_with_id.json',
         '/hd4T/yanghongkai/recorder_server_data/dc_recorder/phonenumber_with_id.json',
         '/hd4T/yanghongkai/recorder_server_data/dc_recorder/db.sqlite'),
    ]:
        handle = BaseHandleDBD(db_path=db_path)
        a = handle.load_data_from_db(json_file)
        print(a)
        # handle.merge_json(json_lc=json_file,json_db_stem=json_db_stem, special=None)