import pymsql
from dingdian import settings

conn = pymysql.connect(user = "root", password = "qingyi", host = "127.0.0.1", database = "paider",  port = 3306, charset = "utf8")
cur = conn.cursor()

class Sql:

    @classmethod
    def insert_dd_name(cls, xs_name, xs_author, category, name_id):
        cur.execute('insert into dd_name (xs_name, xs_author, category, name_id) values(%s, %s, %s, %s)'
        ,(xs_name, xs_author, category, name_id))
        conn.commit()

    @classmethod
    def select_name(cls, name_id):
        sql = 'select exists(select 1 from dd_name where name_id = %s)',(name_id)
        cur.execute(sql)
        return cur.fetchall()[0]