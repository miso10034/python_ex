import pickle, os # 리스트 안에 클래스가 들어있기 때문에 텍스트 형식으로 저장할 수 없다.
from Account import Account # 로직을 클래스와 연결해주는 것 Account.deposit()
# import Account                                         Account.Account.deposit()
# from Account까지는 어카운트 파일에 접근 import Account는 어카운트 클래스를 가져다 쓰겠다.

path = os.path.dirname(__file__)
account_list=[] #빈파일에 아래의 피클로 파일을 저장하고 불러옴

# with open(path +'/account.pickle','rb') as f:
#     account_list = pickle.load(account_list,f)

result=list(map(lambda x:x.account_number,account_list)) # 첫번째인자값은 함수->account_number
Account.account_count = max(result) 


while True:
    display = ''' 
----------------------------------------------------------------------------
1. 계좌개설  2. 입금  3. 출금  4. 계좌로그  5. 계좌정보  6. 계좌리스트  7. 종료
----------------------------------------------------------------------------
>>>   '''
    menu = input(display)
    if menu == '1': 
        name = input('이름 >>> ')
        check = 0
        for item in account_list:
            if item['name'] == name:
                check = 1
        if check == 0:
                break
        balance = '' # 맨처음 금액이 비어있기 때문에 아래의 조건을 만족한다.
        while not balance.isdecimal(): #숫자가 아닐경우에 다시 입력받게끔
            balance = input('입금금액 >>> ')
        balance = int(balance)
        account_list.append(Account(name,balance))#계좌를 개설해서 이름과 금액을 넣어 리스트에 저정해서 만든다
        print('-'*50)
        for item in account_list:
            print(item) #뭐가 들었는지 확인하는 용도

    elif menu == '2':
        if account_list == None:
            print('account를 생성한 후 입금 가능합니다.')
        else:
            name = input('계좌의 명의자를 입력하세요')
            bankcard = Account.bankcard(account_list,balance)
        pass
    elif menu == '3':
        if account_list == None:
            print('account를 생성한 후 입금 가능합니다.')
        else:
            bankcard = bankcard.account.withdraw()
        pass
    elif menu == '4':
        if account_list == None:
            print('account를 생성한 후 입금 가능합니다.')
        pass
    elif menu == '5':
        if account_list == None:
            print('account를 생성한 후 입금 가능합니다.')
        else:
            print(list(account_list.name.keys()))
            name = input('account name >>> ')
            print(name)
    elif menu == '6':
        if account_list == None:
            print('account를 생성한 후 입금 가능합니다.')
        else:
            key = input('계좌리스트(name,balance,total_log)')
            sort = bool(input('오름차순(enter),내림차순(1) >>>'))
            if key in ('name','balance','total_log'):
                Account.displayinfo(key,sort)
            else: #아무것도 안넣으면 여기로
                 Account.displayinfo(reverse=sort)

    elif menu == '7':
        print('프로그램 종료')
        break
    else:
        print('메뉴를 잘못 선택하셨습니다.')

# with open(path +'/account.pickle','wb') as f:
#     pickle.dump(account_list,f)#파일형태로 저장하는 거 아니니까 dumps로 하면 안된다.