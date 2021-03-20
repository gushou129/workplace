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
    def hashes_exists(self, addons):
        where = []

        for idx, sha in addons:
            where.append(and_(hash_table.c.addonid == idx,
                              hash_table.c.sha256 == sha,
                              hash_table.c.registered == 1))

        query = select([hash_table.c.addonid,
                        hash_table.c.sha256]).where(or_(*where))
        res = self._safe_execute(query)
        try:
            return res.fetchall()
        finally:
            res.close()
'''
# 引入sqlalchemy.sql的select模块，从$hash_table$表中选取$hash_table.c.addonid$, $hash_table.c.sha256$和$hash_table.c.registered$列中$hash_table.c.addonid$等于$addonid$的序列存入$res$中，尝试返回$res$所有列，最后关闭$res$
from sqlalchemy.sql import select
def hashes_exists(conn, hash_table,addonid):
    query = select(hash_table).where(hash_table.c.addonid == addonid)
    res = conn.execute(query)
    try:
        return res .fetchall()
    finally:
        res.close()
