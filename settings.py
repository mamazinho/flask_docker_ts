from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

class Settings:

    # Engine = create_engine('postgresql://postgres:olist123@172.17.0.2:5432/orders', echo=False)
    # Engine = create_engine('postgresql://olist:olist123@orders:5432/orders', echo=False)
    Engine = create_engine('mysql://olist:olist123@ts_mysql:3306/orders', echo=False)
    # Engine = create_engine('sqlite:///database.db', echo=False) SQLite3 project
    Base = declarative_base()
    
