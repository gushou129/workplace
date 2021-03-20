'''
useful : 1

原始代码如下所示，请注意:
1）原始的注释和代码存在于多行注释中，改造后的代码应该写在注释以外，并保证代码不会出现依赖错误；
2）如果代码因为无法改造导致的无法使用，请不用在注释外添加内容，且将注释开头的useful标注为0；
3）代码改造以后尽量保证代码美观和缩进信息正确，且一次缩进为4个空格；
4）可以对注释中的代码进行修改，但最终改造结果需要保存在注释以外。

comment:
no comments

code:
def create():
    engine = sqlalchemy.create_engine(db_url('postgres'))
    conn = engine.connect()
    conn.execute('COMMIT;')
    conn.execute('CREATE DATABASE geochat;')
    conn.execute('CREATE ROLE geochat WITH LOGIN;')
    conn.execute('GRANT ALL ON DATABASE geochat TO geochat;')
    conn.close()
    _log.info('Created database.')

    engine = get_engine()
    conn = engine.connect()
    conn.execute('CREATE EXTENSION postgis;')
    conn.close()
    _log.info('Created postgis extensions.')
'''
# 使用$db_url$初始化数据库连接，用$conn$连接数据库，执行SQL语句(从$geochat$选取所有列)，并存入 cope 中，断开连接,最后输出$cope$.
import sqlalchemy
def create(db_url,geochat):
    engine = sqlalchemy.create_engine(db_url)
    conn = engine.connect()
    cope = conn.execute("SELECT * FROM postgis where geochat = :geochat", {"geochat": geochat}).fetchall()
    conn.close()
    print(cope)
