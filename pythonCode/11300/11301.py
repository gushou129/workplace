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
def create_database():
    log_start('create_database')
    global DATABASE_SERVER
    global DATABASE_SERVER_URI
    global DATABASE_NAME
    global DATABASE_URI

    dbserver_engine = sqlalchemy.create_engine(DATABASE_SERVER_URI, pool_recycle=180) # connect to server
    existing_databases = dbserver_engine.execute("SHOW DATABASES;")
    existing_databases = [d[0] for d in existing_databases]
    # for database in existing_databases:
    #     print("...database {0} on dbserver {1}".format(database, DATABASE_SERVER_URI))
    if DATABASE_NAME not in existing_databases:
        dbserver_engine.execute("CREATE DATABASE {db}".format(db=DATABASE_NAME))
        log_warning("{0} database CREATED on DBserver {1}".format(DATABASE_NAME, DATABASE_SERVER))
    else:
        log_info("database {0} already exists on DBserver {1}".format(DATABASE_NAME, DATABASE_SERVER))
    # -or-
    # dbserver_engine.execute("CREATE DATABASE IF NOT EXISTS {db}".format(db=DATABASE_NAME))
    # dbserver_engine.execute("USE {db}".format(db=DATABASE_NAME))
    dbserver_engine.dispose()
    log_finish('create_database')
'''
# 使用$conn$查询DATAVASES中DATABASE_SERVER为$DATABASE_SERVER$和DATABASE_URI为DATABASE_URI中含有*的单挑序列，传递给log_start并返回。
def create_database(conn,DATABASE_SERVER,DATABASE_URI):
    sql = "select * from DATABASES where DATABASE_SERVER=:DATABASE_SERVER and DATABASE_URI=:DATABASE_URI"
    log_start = conn.excute(sql,{"DATABASE_SERVER":DATABASE_SERVER,"DATABASE_URI":DATABASE_URI}).fetchone()
    return log_start

