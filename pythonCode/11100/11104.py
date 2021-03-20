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
    def values(self):
        s = select([self.table.c.value])
        res = self.db.execute(s)
        result = res.fetchall()
        result = [x[0] for x in result]  # unpack from per-row
        return result
'''
#使用Python表达式的方式设置SQL（通过$col$查询$table$中的value列），执行SQL并获取所有数据。将查询结果每一项的第0个元素存储为list并返回。
#导入模块sqlalchemy.sql的select函数
from sqlalchemy.sql import select
#定义一个叫values的函数，并传递三个参数
def values(conn,table,col):

    sql = select(table.c.value).where(table.c.col == col)

    reccol = conn.execute(sql).fetchall()

    result = [x[0] for x in reccol]

    return result