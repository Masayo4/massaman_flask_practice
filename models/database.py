from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

database_file = os.path.join(os.path.abspath(os.path.dirname(__file__)),'onegai.db') #DBファイルを定義する
engine = create_engine('sqlite:///'+database_file,convert_unicode=True) #DBファイルの作成,上記のpath参照
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine)) #DB接続のインスタンス作成
Base = declarative_base() #Baseオブジェクト作成
Base.query = db_session.query_property() #DBに格納する

def init_db():
    import models.models
    Base.metadata.create_all(bind=engine) #DBのイニシャライズ
