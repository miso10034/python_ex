class Test: #클래스는 하나의 변수만 가질 수 있다.
    count=0 #클래스를 만들면서 변수를 선언해주고 싶을 때 __init__(self)이렇게 쓴다.
    def __init__(self,age=7,*name) -> None: # 객체 생성시 초깃값을 받을 때 사용 (self)첫번쨰 인자값은 무조건 self를 받는다
       self.name = name # 인스턴스당 따로 갖고 있는 변수
       self.age = age
       Test.count += 1
       self.count = Test.count

    def __str__(self): #클래스에 있는 모든 함수는 처음에 self를 붙여야 한다
        return f'Test class [{self.name},{self.age},{self.count}]'

test01 = Test(7,'홍길동','김철수') #객체를 생성할 때 누구를 호출? __init__
print(type(test01))
print(test01)

# test02 = Test('홍길동',22)
# print(test02.name,test02.age)
# test03 = Test('박철우',21)
# print(test03.name,test03.age)
# test02.age = 34
# print(test02.name,test02.age)

# test02 = Test('홍길동',22)
# test03 = Test('박철우',21)
# Test.count+=1
# test02.count +=1 # 이렇게하면 바로 아래만 적용이 된다.
# Test.count +=1 #클래스이름 점count로만 모두에게 적용이 된다.
# print(Test.count)
# print(test02.count)
# print(test03.count)

# test02 = Test('홍길동',22)
# test03 = Test('박철우',21)
# test04 = Test('박철',21)
# print(test02.count)
# print(test03.count)
# print(test04.count)