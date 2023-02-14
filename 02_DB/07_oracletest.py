import cx_Oracle

conn = cx_Oracle.connect('SCOTT/TIGER@localhost:1521/xe')#어디로 접속할 것인지 써줘야함

cur = conn.cursor()

sql = 'select * from emp'

cur.execute(sql)
for item in cur.fetchall():
    print(item)

conn.close()