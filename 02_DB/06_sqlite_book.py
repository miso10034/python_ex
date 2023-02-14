import book 

book.create_table() #테이블이 없으면 생성하고 있으면 있는거 갖다 쓰기
while True:
    prompt = '''
----------------------------------------------------------------------
1.책정보 등록 2.책정보 수정 3.책정보 삭제  4.책 리스트 출력 5. 검색 6.종료
----------------------------------------------------------------------
    '''
    menu = input(prompt)
    if menu == '1':
        try:
            book.insert_books() #데이터 입력함수를 불러온다.
        except Exception as e:
            print(e)
    elif menu == '2':
        book.update_book()
    elif menu == '3':
        book.delete_book()
    elif menu == '4':
        book.all_books()
    elif menu == '5':
        book.big_books()
    elif menu == '6':
        print('프로그램 종료!')
        pass
    else:
        print('메뉴선택을 잘못하셨습니다.')