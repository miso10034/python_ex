import oracledb
oracledb.init_oracle_client()



def create_table():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            sql = '''
            create table customer(
                email varchar2(50) primary key,
                name varchar2(20),
                gender varchar2(2),
                birthyear number(4)
            )
            '''
            try:
                cur.execute(sql)
            except Exception as e:
                print(e)
    
def insert_ct():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            sql = 'insert into customer values(:1,:2,:3,:4)'
            name = input('이름 >>> ')
            gender = input('성별 >>> ')
            birthyear = input('출생연도 >>> ')
            try:
                cur.exectue(sql,(name,gender,birthyear))
            except Exception as e:
                print(e)
def search_ct():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            custlist = []
            for item in cur.execute('select email from customer'):
                custlist.append(item[0])
            print(custlist)
            key = int(input('검색할 이메일 >>> '))
            cur.execute('select * from customer where email =:1,(key,)')
            print(cur.fetchone())
                
def delete_ct():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            custlist = []
            for item in cur.execute('select * from customer'):
                print(f'이메일:{item[0]},이름:{item[1]},성별:{item[2]},출생연도:{item[3]}')
                custlist.append(item[0]) # 키값 모으기
            key = int(input('삭제할 이메일 >>> ')) #어떤거 수정할 것인지
            if key in custlist:
                sql = f'delete namecard where email = :1'
                cur.execute(sql,(key,))
                conn.commit()
def update_ct():
    with oracledb.connect('SCOTT/TIGER@localhost:1521/xe') as conn:
        with conn.cursor() as cur:
            custlist = []
            for item in cur.execute('select*from customer'):
                print(f'이메일:{item[0]},이름:{item[1]},성별:{item[2]},출생연도:{item[3]}')
                custlist.append(item[0])
            key = int(input('수정할 이메일 >>> '))
            if key in custlist:
                col = input('수정할 이메일 >>> ')
                data = input('수정할 값 >>> ')
                sql = f'updata customer set {col}=:1 where cardid =:2'
            cur.execute(sql,(data,key))
            conn.commit()

if __name__=='__main__':
    insert_ct()
    update_ct()
    delete_ct()
    search_ct()
