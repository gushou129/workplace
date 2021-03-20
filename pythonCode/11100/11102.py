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
    def test_reflect_alt_owner_synonyms(self):
        testing.db.execute('CREATE TABLE localtable (id INTEGER '
                           'PRIMARY KEY, parent_id INTEGER REFERENCES '
                           '%s.ptable(id))' % testing.config.test_schema)
        try:
            meta = MetaData(testing.db)
            lcl = Table('localtable', meta, autoload=True,
                        oracle_resolve_synonyms=True)
            parent = meta.tables['%s.ptable' % testing.config.test_schema]
            self.assert_compile(
                parent.join(lcl),
                '%(test_schema)s.ptable JOIN localtable ON '
                '%(test_schema)s.ptable.id = '
                'localtable.parent_id' % {
                    "test_schema": testing.config.test_schema})
            select([parent,
                   lcl]).select_from(parent.join(lcl)).execute().fetchall()
        finally:
            testing.db.execute('DROP TABLE localtable')
'''
#尝试性使用$conn$执行SQL（根据$parent_id$查询localtable表中的所有id）,获取并返回所有结果。最终确保$conn$关闭。
def test_reflect_alt_owner_synonyms(conn,parent_id):
    try:
        texts = conn.execute("SELECT id FROM localtable WHERE parent_id=:parent_id",{"parent_id":parent_id}).fetchall()
        return texts
    finally:
        conn.close()