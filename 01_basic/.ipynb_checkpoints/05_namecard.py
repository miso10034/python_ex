card=[['홍길동', '서울','111-1111-1111','hong@gmail.comm'],
      ['김나리', '광주','111-1111-1112','kim@gmail.comm']]
while True:
    menu = input('''
--------------------------------------------------
1.저장  2.수정  3.삭제  4.리스트  5.검색  6.종료(Q)
--------------------------------------------------
>>>''')
    if menu == '1':
        while True:
            name = input('이름을 입력하세요 >>>')
            check = 0
            for item in card:
                if item[0] == name:
                    check = 1
            if check == 0:
                    break
            print('중복되는 이름이 있습니다.')
                
        address = input('주소를 입력하세요 >>>')
        tel = input('전화번호를 입력하세요 >>>')
        email = input('이메일을 입력하세요 >>>')
        card.append([name,address,tel,email])
        print(card)  
    if menu == '1':
        pass
    elif menu == '2':
        pass
    elif menu == '3':
        pass
    elif menu == '4':
        pass
    elif menu == '5':
        pass
    elif menu == '6':
        print('프로그램 종료')
        break
    else:
        print('메뉴선택을 잘못하셨습니다.')