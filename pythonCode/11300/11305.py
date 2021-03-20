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
    def test_contains_doesnt_compile(self):
        row = t.select().execute().first()
        c1 = Column("some column", Integer) + Column(
            "some other column", Integer
        )

        @profiling.function_call_count()
        def go():
            c1 in row

        go()
'''
# 执行SQL语句（从$column$表中选取所有列），返回获取集的下一行单个序列
def test_contains_doesnt_compile(conn,column):
    row = conn.execute("SELECT * FROM Column where column = :column", {"column": column}).fetchone()
    return row
