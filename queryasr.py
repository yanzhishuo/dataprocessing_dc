import argparse
from datetime import datetime
import json
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 变动代码位置需改这里
from models import Data


class BaseHandleDBD:

    def __init__(self,db_path):

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
