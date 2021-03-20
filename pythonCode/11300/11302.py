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
    def test_insert_multiple_rows_one_commit(self):
        riders = [{'id': 1}, {'id': 2}, {'id': 3}]
        with session_scope(commit=False) as session:
            for rider in riders:
                get_or_create(session,  Riders, commit=False, **rider)
            session.commit()
        result = self.cur.execute('SELECT * FROM RIDERS').fetchall()
        self.assertTrue(tuple(r[0] for r in result) == y['id'] for y in riders)
'''
# 执行SQL语句（选取$rider$中所有列)存入$result$,输出一个储存每一列的第0号元素的元组
def test_multiple_rows_one_commit(conn,rider):
    result = conn.execute("SELECT * FROM RIDERS where rider = :rider",{"rider":rider}).fetchall()
    return tuple(r[0] for r in result)
