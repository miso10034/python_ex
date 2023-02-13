import pickle, os # 경로명때문에 os/리스트 안에 클래스가 들어있기 때문에 텍스트 형식으로 저장할 수 없다.
from Account import Account ,str2int# 로직을 클래스와 연결해주는 것 Account.deposit()
# import Account                                         Account.Account.deposit()
# from Account까지는 어카운트 파일에 접근 import Account는 어카운트 클래스를 가져다 쓰겠다.

path = os.path.dirname(__file__)#현재실행되는 경로를 갖고 있다
account_list=[] #빈파일에 아래의 피클로 파일을 저장하고 불러옴

with open(path +'/account.pickle','rb') as f:
    account_list = pickle.load(account_list,f)

result=list(map(lambda x:x.account_number,account_list)) # 첫번째인자값은 함수->account_number
Account.account_count = max(result) 
# x에 있는 account_number를 빼서 리스트로 저장해서 결과처리중 가장 큰값


while True:
    display = ''' 
----------------------------------------------------------------------------
1. 계좌개설  2. 입금  3. 출금  4. 계좌로그  5. 계좌정보  6. 계좌리스트  7. 종료
----------------------------------------------------------------------------
>>>   '''
    menu = input(display)
    if menu == '1': 
        name = input('이름 >>> ')
        balance = str2int('입금할 금액을 입력하세요')
        # balance = '' # 맨처음 금액이 비어있기 때문에 아래의 조건을 만족한다.
        # while not balance.isdecimal(): #숫자가 아닐경우에 다시 입력받게끔
        #     balance = input('입금금액 >>> ')
        # balance = int(balance)
        account_list.append(Account(name,balance))#계좌를 개설해서 이름과 금액을 넣어 리스트에 저정해서 만든다
        print('-'*50)
        for item in account_list:
            print(item) #뭐가 들었는지 확인하는 용도

    elif menu == '2': #어떤 계좌에 대한 입금처리냐
        account_num =str2int('계좌번호를 입력하세요')
        check = 0 #계좌가 있는지 없는지
        for acc in account_list:
            if acc.account_number == account_num:
                check = 1
                amount = int(input('입금할 금액을 입력하세요 >>>'))
                acc.deposit(amount) #호출
                break #for문 벗어남
        if check == 0:
            print('계좌번호가 없습니다.')

    elif menu == '3': #출금
        account_num = str2int('계좌번호를 입력하세요')
        check = 0 #계좌가 있는지 없는지
        for acc in account_list:
            if acc.account_number == account_num:
                check = 1
                amount = int(input('출금할 금액을 입력하세요 >>>'))
                acc.withdraw(amount) #호출
                break #for문 벗어남
        if check == 0:
            print('계좌번호가 없습니다.')
            
    elif menu == '4': #계좌로그 특정계좌에 대한 로그를 찍어야한다.
        account_num = str2int('계좌번호를 입력하세요')
        check = 0 #계좌가 있는지 없는지
        for acc in account_list:
            if acc.account_number == account_num:
                check = 1
                print(acc.total_log)
                break #for문 벗어남
        if check == 0:
            print('계좌번호가 없습니다.')
            
    elif menu == '5':
        account_num = str2int('계좌번호를 입력하세요')
        check = 0 #계좌가 있는지 없는지
        for acc in account_list:
            if acc.account_number == account_num:
                check = 1
                print(acc) # acc를 찍으면__str__이 동작한다.
                break #for문 벗어남
        if check == 0:
            print('계좌번호가 없습니다.')
    elif menu == '6':
        key = input('정력 키 (입력값:name,balance,account_number) >>>')
        sort = bool(input('오름차순(enter),내림차순(1) >>>'))
        if key in ('name','balance','account_num'): # 입력받은 값중 있느냐
            sorted_list = sorted(account_list,reverse=sort,key=eval(f'lambda x : x.{key}')) #있으면 이걸로 정렬 #키는 람다함수로 받음
        else: #없으면 이걸로                                       
            sorted_list = sorted(account_list,reverse=sort)
        # 네임카드 클래스는 한장한장 관리하고 카드북클래스로 여러개를 관리
        # 은행 관리시스템은 하나의 클래스가 관리
        for acc in sorted_list: #리스트에 있는 sort를 하면 원본을 처리하는데 우리는 원본을 사용하지않는다.
            print(acc)#__str__이 동작하게된다.

    elif menu == '7':
        print('프로그램 종료')
        break
    else:
        print('메뉴를 잘못 선택하셨습니다.')

with open(path +'/account.pickle','wb') as f:
    pickle.dump(account_list,f) #파일형태로 저장하는 거 아니니까 dumps로 하면 안된다.
