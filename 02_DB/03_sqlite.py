import sqlite3,os

path = os.path.dirname(__file__)
conn = sqlite3.connect(path + '/example.db') 
cur = conn.cursor() 
# select * from stocks where symbol = 'rhat'
symbol = input('종목이름을 입력하세요 >>> ')
sql = "select * from stocks where symbol = :1" #중괄호로 나온다.데이터타입은 상관없다. #물음표는 위치
# sql = "select * from stocks where symbol = '%s'" % symbol
#select문이라서 커밋할 필요는 없다        #sqlite에서 이것이 가능하다.
cur.execute(sql,(symbol,)) #데이터는 한건으로 나와야한다 리스트로 묶던 튜플로 묶던 해야한다. 
#튜플은 값을 하나줄때 ,를 붙여야한다. 뒷내용을 붙이지 않더라도 /리스트는 []/튜플(하나일때,)
print(cur.fetchone())
 #패치매니는 갯수를 설정할 수 있다.
 #패치원은 하나만 나오니까 굳이 for문을 돌릴 필요가 없다.
conn.close()