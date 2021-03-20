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
def get_casino_bars(casino):

	get_bars = sql.text("SELECT Bar FROM Bars WHERE Casino=:c;")

	rs = con.execute(get_bars, c=casino)

	return [dict(row) for row in rs]

'''
# 执行SQL语句（根据$Casino$获取Barstable中的全部Bar），将查询结果每一项转化为dict存储为list并返回。
def query_page(conn,Casino):
    Bars = conn.execute("SELECT Bar FROM Barstable WHERE Casino=:Casino",{"Casino":Casino}).fetchall()
    return [dict(row) for row in Bars]