#import할떄 라이브러리와 똑같은 이름을 해놓으면 안된다.
import sqlite3 #sql에서 sqlite를 쓸 수 있는 라이브러리 
               #파일로 저장이 되서 계정과 관련된(보안)은 없다
import os
print(sqlite3.version)
print(sqlite3.sqlite_version) 
path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '/example.db') #db랑 연결하겠다. 괄호 안에 파일 이름 확장자는 크게 상관이 없다.
cur = conn.cursor()                          #있으면 그거 쓰고 없으면 새로 만든다.
cur.execute(''' 
create table if not exists stocks 
(date text,trans text,symbol text,qty real,price real)
''') #실행 쿼리문을 동작하게 하는것
cur.execute(''' 
insert into stocks values('2023-01-02','buy','rhat',100,35.23)
''')#주식 디비
conn.commit()# 변화가 있는 것은 커밋을 꼭 해줘야한다.
conn.close()