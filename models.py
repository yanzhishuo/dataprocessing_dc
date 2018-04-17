import os
import sqlalchemy
import yaml
from sqlalchemy import (Column,
                        ForeignKey,
                        Integer,
                        String,
                        Text,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (sessionmaker,
                            relationship,
                            backref)

import config

Base = declarative_base()

db_path = config.db_filename
if not db_path.startswith('/'):
    db_path = os.path.join(os.path.dirname(__file__), db_path)

engine = create_engine('sqlite:///{}'.format(db_path))
session = sessionmaker()
session.configure(bind=engine)


def get_engine(db_dir):
    engine = create_engine('sqlite:///{}'.format(os.path.join(db_dir, config.db_filename)))
    if not engine.dialect.has_table(engine, 'data'):
        Base.metadata.create_all(engine)
    return engine


def get_session(engine):
    session = sessionmaker()
    session.configure(bind=engine)
    return session()


class Data(Base):

    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    ref = Column(String, nullable=False)
    asr = Column(String, nullable=True)
    json_file_stem = Column(String, nullable=False, primary_key=True)

    def to_dict(self):
        return dict(
            id=self.id,
            ref=self.ref,
            asr=self.asr,
            json_file_stem=self.json_file_stem,
        )

    def __repr__(self):
        return '<Data id={!r} ref={!r} asr={!r} in "{!s}.json"'.format(
            self.id, self.ref, self.asr, self.json_file_stem)


if not engine.dialect.has_table(engine, 'data'):
    Base.metadata.create_all(engine)

s = session()
# for i in range(10):
#     d = Data(id=i, ref='引用:{}'.format(i), json_file_stem='json_file_1')
#     s.add(d)
# s.commit()

print(s.query(Data).filter(Data.json_file_stem == 'json_file_1').all())
