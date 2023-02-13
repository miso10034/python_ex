# 책정보를 저장하는 테이블
''' 
books
 - title 책제목 텍스트
 - published_data 출판날짜 텍스트
 - publisher 출판사 텍스트
 - pages 페이지수 정수
 - recommend 추천여부 정수
'''

'''
create table if not exists books(
    title text,
    published_data text,
    publisher text,
    pages integer,
    recommend integer
)
'''
import sqlite3,os

path = os.path.dirname(__file__)

# 테이블 생성 함수
def create_table():
    conn = sqlite3.connect(path + '/example.db') 
    cur = conn.cursor()
    cur.execute(
    '''
    create table if not exists books(
    title text,
    published_data text,
    publisher text,
    pages integer,
    recommend integer)'''
    )
    conn.commit()
    conn.close()

create_table()

# 데이터 입력 함수
def insert_books():
    conn = sqlite3.connect(path + '/example.db') 
    cur = conn.cursor()
    title = input('제목 >>> ')
    published_data = input('출판일 >>> ')
    publisher = input('출판사 >>> ')
    pages = input('총 page >>> ') #int를 안써줘도 된다.
    recommend = input('추천수 >>> ')
    sql = 'insert into books values(?,?,?,?,?)'
    cur.execute(sql,(title,published_data,publisher,pages,recommend))
    conn.commit()
    conn.close()

# insert_books()

# 전체데이터 출력 함수
def all_books():
    conn = sqlite3.connect(path + '/example.db') 
    cur = conn.cursor()
    sql = 'select * from books'
    cur.execute(sql)
    for item in cur.fetchall():
        print(item)
    conn.close()

# all_books()

# 레코드 갯수를 정해서 출력
def some_books(number):
    conn = sqlite3.connect(path + '/example.db') 
    cur = conn.cursor()
    sql = 'select * from books'
    cur.execute(sql)
    for item in cur.fetchmany(number):
        print(item)
    conn.close()

# number =int(input('출력할 데이터 갯수 >>> '))
# some_books(number)
# 한권만 출력
def one_books():
    pass

# 조건 지정 및 정렬하여 검색
# 정렬(asc,desc)
def big_books(key='title', sort='asc', cond =''):
    conn = sqlite3.connect(path + '/example.db')
    cur = conn.cursor()
    if cond != '': #빈 문자열이 아니면
        cond = 'where '+ cond 
    sql = f'select * from books {cond} order by {key} {sort}'
    cur.execute(sql)
    for item in cur.fetchall():
        print(item)
    conn.close()

# big_books('pages','desc','pages>= 300')
big_books('pages','desc',"title like '%머신%' ")

# 책은 title로 구분
# 책 수정 
#  - title 책제목 텍스트
#  - published_data 출판날짜
#  - publisher 출판사
#  - pages 페이지수
#  - recommend 추천여부
def update_book(key='title'):
    conn = sqlite3.connect(path + '/example.db')
    cur = conn.cursor()
    all_books() # 호출시 전체목록이 찍힌다.
    title = input('수정할 책 제목 >>> ')
    check = 1
    while check:
        col = input('수정할 컬럼이름(published_data,publisher,pages,recommend) >>> ')
        if col in ('published_data','publisher','pages','recommend'):
            check = 0
    value = input(f'{col}컬럼 수정할 내용 입력 >>> ') #해당컬럼에 수정할내용 받아줘
    sql = f'update books set {col} = ? where title = ? '
    cur.execute(sql,(value,title))
    conn.commit()
    conn.close()

# update_book()

# 책 삭제
def delete_book():
    conn = sqlite3.connect(path + '/example.db')
    cur = conn.cursor()
    all_books() 
    title = input('삭제할 책 제목 >>> ')
    sql = f'delete from books where title = ?'
    cur.execute(sql,[title])
    conn.commit()
    conn.close()

delete_book()