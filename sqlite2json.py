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
                 db_path,
                 save_dir='/hd4T/yanghongkai/wulumuqi/db2json'):
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

    def load_data_from_db(self,
                          json_file,
                          save_path=False):
        json_file = pathlib.Path(json_file)
        json_file_stem = json_file.stem
        json_file_name = json_file.name
        # 以文件名(不带拓展为依据)读数据
        json_list_db = []
        raw_db = self.session.query(Data).filter(
            Data.json_file_stem == json_file_stem).order_by(Data.id).all()
        for data in raw_db:
            _dict = dict()
            _dict['id'] = data.id
            _dict['ref'] = data.ref
            _dict['asr'] = data.asr
            json_list_db.append(_dict)
        if save_path and isinstance(save_path, bool):  # save_path = True
            save_dir = self.save_dir
            save_dir.mkdir(parents=True, exist_ok=True)
            save_path = save_dir.joinpath(json_file_name)
            self.save_json(json_list_db, str(save_path))  # save path include file name
        elif save_path and isinstance(save_path, str):
            self.save_json(json_list_db, save_path)
        return json_list_db

    def merge_json(self, json_lc, json_db_stem, json_db=True, special='gym'):
        """Default merge with db2json fold's file with same name."""
        json_lc = pathlib.Path(json_lc)
        json_list_lc = self.load_data_from_local(str(json_lc))
        if special:
            print('do special json_lc')
            json_list_lc = self.special4gym(json_list_lc)
        if json_db and isinstance(json_db, bool):
            print('load json_db from db')
            json_list_db = self.load_data_from_db(json_db_stem, save_path=False)
        elif json_db and isinstance(json_db, str):
            print('load json_db from local')
            json_list_db = self.load_data_from_local(json_db)
        else:
            print('json_db is True or db path')
            exit()
        if len(json_list_lc) != len(json_list_db):
            print('json_lc', len(json_list_lc))
            print('json_db', len(json_list_db))
            print("Error: merge json length different!")
            exit()
        else:
            json_lc_name = json_lc.name
            save_dir = self.save_dir
            save_dir.mkdir(parents=True, exist_ok=True)
            save_path = save_dir.joinpath(json_lc_name)
            _json_list = list()
            for n in range(len(json_list_lc)):
                json_list_lc[n].update(json_list_db[n])
                _json_list.append(json_list_lc[n])
            self.save_json(_json_list, str(save_path))

    @staticmethod
    def load_data_from_local(json_file):
        with open(json_file) as f:
            lc_json_list = json.load(f)
        return lc_json_list

    @staticmethod
    def special4gym(json_list):
        for _dict in json_list:
            for k, v in _dict.items():
                if v == "None":
                    _dict[k] = ''
        return json_list

    @staticmethod
    def save_json(json_list, save_path):
        with open(str(save_path), 'w') as fp:
            json.dump(json_list, fp, ensure_ascii=False, indent=4)


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
        handle.merge_json(json_lc=json_file,json_db_stem=json_db_stem, special=None)
