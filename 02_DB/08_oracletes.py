import cx_Oracle

try:
    conn = cx_Oracle.connect('SCOTT/TIGER@localhost:1521/xe')#어디로 접속할 것인지 써줘야함
    cur = conn.cursor()
    sql = 'insert into dept values(:1,:2,:3)' # :1, ? 모두 가능
    data = (50,'DATABASE','SEOUL')
    cur.execute(sql,data)
    conn.commit()
    conn.close()
except Exception as e:
    print(e)
    print('중복되는 값입니다.')

print('계속진행!!!')