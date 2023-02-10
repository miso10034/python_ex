import cardfunc as cf
import pickle

bookcard = None
#card=[['17890', 'c언어 정복하기','한빛'],
#     ['67890','파이썬을 잡아라','아카데미']]

while True:
    menu = input('''
----------------------------------------------------------------------------------------
1.CardBook저장  2.CardBook수정  3.CardBook삭제  4.CardBook리스트  5.전체목록보기  6.종료(Q)
>>>''')
    if menu == '1':
        if bookcard ==None:
            cardbook = nc.CardBook(input('타이틀을 입력하세요 >>>'))
        else:
            print('생성된 bookcard가 존재합니다.')

    elif menu == '2':
        if cardbook ==None:
            print('cardbook 생성한 후 추가 가능합니다.')
        else:
            bookname = input('bookname >>>')
            booknumber = input('booknumber >>>')
            bookoriented = input('bookoriented >>>')
            card = cf.Card(bookname,booknumber,bookoriented)
            bookcard.add_card(card)
            
    elif menu == '3':
        if bookcard == None:
            print('bookcard 생성 후 가능합니다.')
        else:
            print(list(bookcard.cards.keys()))
            b_name = int(input('bookname >>>'))
            card = bookcard.remove_card(b_name)
            print(card,'-> 삭제')

    elif menu == '4':
        if bookcard == None:
            print('bookcard 생성한 후 가능합니다.')
        else:
            print(list(bookcard.cards.keys()))
            b_name = int(input('b_name >>>'))
            card = bookcard.cards[b_name]
            print(card)

    elif menu == '5':
        if cardbook == None:
            print('bookcard 생성한 후 가능합니다.')
        else:
            key = input('정렬 키(입력값:bookname,booknumber,bookoriented) >>>')
            sort = bool(input('오름차순(enter),내림차순(1) >>>'))
        if key in ('bookname','booknumber','bookoriented'):
            bookcard.list_cards(key,sort)
        else:
            cardbook.list_cards(reverse=sort)

    elif menu == '6':
        print('프로그램 종료')
        break

with open('01_basic/bookcard.pickle','wb') as f:
    pickle.dump(cardbook,f)