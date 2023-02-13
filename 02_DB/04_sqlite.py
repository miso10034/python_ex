import sqlite3,os

path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '/example.db') 
cur = conn.cursor() 
sql = 'insert into stocks values(?,?,?,?,?)'
# data = ('2022-01-08','buy','ibm',1000,45.00)
# cur.execute(sql,data) #execute는 딱 1건에 대한 실행이다.
data = [('2022-01-08','buy','ibm',1000,45.00),
        ('2022-02-11','sell','ibm',500,48.00),
        ('2022-03-08','buy','msft',400,72.00),
        ('2022-07-20','buy','rhat',120,37.00),
        ('2022-11-08','sell','rhat',150,45.00),]
cur.executemany(sql,data) #executemany이면 data 갯수도 똑같이 설정해줘야한다.
conn.commit()
conn.close()