import oracledb
oracledb.init_oracle_client()

try:
    conn = oracledb.connect('SCOTT/TIGER@localhost:1521/xe')
    cur = conn.cursor()
    cur.execute('select * from dept')
    print(cur.fetchall())
    sql = 'delete from dept WHERE DEPTNO = :1 '
    deptno = input('삭제할 부서코드 >>>')
    data = (deptno,) #튜플일때 하나일 경우 꼭 , 붙이기
    cur.execute(sql,data) 
    conn.commit()
    conn.close()
except Exception as e:
    print(e)