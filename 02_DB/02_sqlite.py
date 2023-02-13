import sqlite3,os

path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '/example.db') 
cur = conn.cursor() 
# 결과값은 커서가 갖고 있따.
cur.execute(''' 
select * from stocks
''')
# print(cur.fetchall()) #다 들고 오면 fetchall 결과가 여러개니까 결과를 list로 반환
# 주석처럼 처리하면 튜플로 결과값이 반환되서 튜플의 특징인 중간 수정이 안된다
for item in cur.fetchall():
    print(item[0],item[1],item[2],item[3],item[4]) #튜플이니까 인덱스로 접근이 가능하다

conn.close()