from sqlalchemy import Column, String Integer, create_engine
form sqlalchemy.orm import sessionmaker
form sqlalchemy.ext.declarative import declarative_base

# 创造对象的基类
Base = declarative_base()
