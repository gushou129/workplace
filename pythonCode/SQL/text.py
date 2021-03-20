from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类：
Base = declarative_base()

class Person(Base):

    #表名
    __tablename__ = 'texttable'

    # 表结构
    id = Column(Integer(), primary_key = True)
    name = Column(String(45))
    sex = Column(String(45))

    def __init__(self, id, name, sex):
        self.id = id
        self.name = name
        self.sex = sex

# 初始化数据库连接：
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/textdb', echo = True)

# 创建DBSession类型：
DBSession = sessionmaker(bind = engine)

session = DBSession()

# # 增操作，增加三条记录
# item1 = Person(id=1, name='xgx', sex='male')
# session.add(item1)

# item2 = Person(id=2, name='xgx1', sex='female')
# session.add(item2)

# item3 = Person(id=3, name='xgx2', sex='female')
# session.add(item3)

# item4 = Person(id=4, name='xgx', sex='female')
# session.add(item4)

# session.commit()
# session.close()

# 查操作
# session1 = DBSession()
# persons = session1.query(Person).filter(Person.id < '4').all()

# for i in range(len(persons)):
#     print(persons[i].id)
#     print(persons[i].name)
#     print(persons[i].sex)

# print('*********')

# for row in session1.query(Person, Person.name).all():
#     print(row.Person, row.name)

# session1.close()

# # 改操作，将id为2的记录的service_name字段修改为movie
# session2 = DBSession()
# session2.query(Person).filter(Person.id == '2').update({Person.name: 'xxx'}, synchronize_session)