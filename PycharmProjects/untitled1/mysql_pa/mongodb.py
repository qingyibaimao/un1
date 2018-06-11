# -*- coding: utf-8 -*-

import pymysql

conn = pymysql.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'qingyi', db = 'panode')
cur = conn.cursor()
sql = '''
    create table person(
      id int not null,
      name varchar(20),
      age int
    );
'''
select_sql = '''
    select * from person;
'''
cur.execute(select_sql)
for r in cur.fetchall():
    print(r)
#cur.executemany('insert into person (id, name,age) values (%s, %s, %s)', [(1,'zhang', 19), (2,'hui',18), (3,'jie', 21)])
#conn.commit()
#conn.rollback()

conn.close()