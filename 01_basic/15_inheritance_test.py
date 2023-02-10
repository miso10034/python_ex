class Person: #인잇은 개체가 생성되는 시점에 생성된다.
    def __init__(self,name,age,gender) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self):
        print('저의 이름은',self.name,'이고요, 제 나이는 ',self.age,'살입니다.')        

class Animal:
    def talk(self):
        print('talk')

class Employee(Person,Animal): #파이썬은 다중상속이 가능하다 상속해서 받은 객체를 리모델링해서 쓰는것 오버라이딩
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name,age,gender)
        self.salary = salary
        self.hire_date = hire_date

    def do_work(self):
        print('열심히 일을 한다.')

    def about_me(self):
        print('제 급여는 ',self.salary,'원이고, 제 입사일은',self.hire_date,'입니다.')
        super().about_me()


        
a1 = Person('김철수',22,'남자')
a2 = Employee('홍길동',33,'남자',2300,'2023/01/01')
a1.about_me()
a2.about_me()
a2.talk() #애니멀에서 상속받은것




# # 클래스 Person 이 korean에게 상속을 준다.
# class Korean(Person):
#     pass
# # 상속을 하면 좋은 점 중복을 피할 수 있다.

# a = Korean('홍길동','33') #인잇에 의해서 네임과 에이지를 받는다
# print(type(a))
# print(a)
# print(a.name)

