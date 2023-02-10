#명암집을 만드는데 설계= 하나하나 명함에 대한 정보 ,명함 정보들을 관리할 수 있는 두개의 클래스로 나눠 관리
#명함한장에 대한 정보, 속성,메서드 / class card는 명함한장에 대한 정보 디폴드 값이 정해져 있지 않아서
#이름,주소,전화번호,이메일 안들어오면 none 값으로 설정

import namecard as nc, os
import pickle

path = os.path.dirname(__file__) #디렉토리에서 디렉토리 이름만 갖고 오기
# print(__file__) #지금 쓰고 있는 파일의 경로와 파일 이름이 찍힌다 ,절대경로
# print(path)
cardbook = None

with open(path+'/cardbook.pickle','rb')as f: ##01_basic을 없애고 path+붙임
    cardbook = pickle.load(f)

while True:
    menu = input('''
---------------------------------------------------------------------------------
1.CardBook 생성  2.Card추가  3.Card삭제  4.Card내용 보기  5.전체목록 보기  6.종료(Q)
---------------------------------------------------------------------------------
>>>''')
    if menu == '1':
        if cardbook == None:
            cardbook = nc.CardBook(input('타이틀을 입력하세요 >>>'))
        else:
            print('생성된 cardbook이 존재합니다.')
    elif menu == '2': 
        if cardbook == None:
            print('cardbook 생성한 후 추가 가능합니다')
        else:
            name = input('name >>>')
            address = input('address >>>')
            tel = input('tel >>>')
            email = input('email >>>')
            card = nc.Card(name,address,tel,email) #인스턴스 생성
            cardbook.add_card(card) 
        
    elif menu == '3':
        if cardbook == None:
            print('cardbook 생성한 후 가능합니다.')
        else:
            print(list(cardbook.cards.keys()))
            page = int(input('page number >>>'))
            card = cardbook.remove_card(page)
            print(card, '-> 삭제')
    elif menu == '4':
        if cardbook == None:
            print('cardbook 생성한 후 가능합니다.')
        else:
            print(list(cardbook.cards.keys()))
            page = int(input('page number >>>'))
            card = cardbook.cards[page]
            print(card)
       
    elif menu == '5':
        if cardbook == None:
            print('cardbook 생성한 후 가능합니다.')
        else:
            key = input('정렬 키(입력값:name,address,tel,email) >>>')
            sort = bool(input('오름차순(enter),내림차순(1) >>>'))
            # print(sort,type(sort))
            if key in ('name','address','tel','email'):
                cardbook.list_cards(key,sort) #넣으면 이쪽으로
            else: #아무것도 안넣으면 여기로
                cardbook.list_cards(reverse=sort)

    elif menu == '6':
        print('프로그램 종료')
        break
  

with open('01_basic/cardbook.pickle','wb') as f:
    pickle.dump(cardbook,f)

