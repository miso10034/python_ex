#클래스 만들고 다른 파일에 로직을 만든다. 이게 클래스
class Account():
    
    account_count = 0 #계좌가 개설된 건수/클래스 변수 전체적인 건수에 추가가 되는 것
                      #초기화가 되는 것이 아니라 인스턴스를 만들지 않아도 접근이 가능하다
#계좌번호는 account_count를 증가시켜서 자동으로 일련번호로 설정할것
    @classmethod
    def get_account_num(cls): #클래스 함수, 메서드 /리턴해주는 함수
        return Account.account_count #객체생성 이전에 클래스에 접근할 수 있는 
                                     #몇개나 계좌가 개설이되었는지 확인한고 싶음
    def __init__(self, name,balance): #balance 입금할 금액
        Account.account_count += 1 # 계좌가 동작하기전에 미리 셋팅을 해놔야해서 여기에
        self.account_number = Account.account_count # 위의 값을 본인의 계좌에 넣는다 계좌번호 생성된것
        self.name = name
        self.balance = balance
        self.total_log = []# 순서대로 로그를 받아야해서 리스트로 받는다 
        self.deposit_count = 0 #이자가 나가는 것도 동작하기 이전에 설정해줘야함
        # 인스턴스마다 초기화되서 처리된다.
    def deposit(self,amonut): #입금처리
        if amonut >= 1:
            self.total_log.append(('임금',amonut)) #로그에 기록
            self.balance += amonut
            self.deposit_count += 1
            print(amonut,'원 입금처리 완료')
            if self.deposit_count % 5 == 0:
                interest = round(self.balance * 0.01,-1) #1의자리수에서 반올림해서 처리
                self.balance += interest
                self.total_log.append(('이자',interest))
                print(interest,'원의 이자가 지급되었습니다.')

    def withdraw(self,amount): #출금처리 출금할 금액
        if self.balance >= amount:
            self.total_log.append(('출금',amount))
            self.balance -= amount
            print(amount,'원 출금처리 완료')
        else:
            print('잔고가 부족합니다.')
        
    def displayinfo(self): #계좌정보출력함수/
        print(self.__str__())#아래꺼를 받아서 출력하는 함수로

    def __str__(self): #예금주, 계좌번호, 잔고에 출력하게해야함 __str__도 무조건 첫번째 인지값으로 self를 줘야함
        return f'예금주:{self.name}, 계좌번호:{self.account_number}, 잔고:{self.balance:>15,}원'

# print(Account.account_count) #클래스 변수와 함수는 클래스당 존재하는 것이다.
print(Account.get_account_num())
a = Account('홍길동',2000)
a.displayinfo()
a.deposit(5000)
a.displayinfo() # 잔고 출력
a.withdraw(4000)
a.displayinfo()
a.withdraw(4000)
print(a.total_log)

