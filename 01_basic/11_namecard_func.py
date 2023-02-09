def save(card): #지역변수
    while True:
        name = input('이름을 입력하세요 >>>')
        check = 0
        for item in card:
            if item['name'] == name:
                check = 1
        if check == 0:
                break
        print('중복되는 이름이 있습니다.')
            
    address = input('주소를 입력하세요 >>>')
    tel = input('전화번호를 입력하세요 >>>')
    email = input('이메일을 입력하세요 >>>')
    card.append({'name':name,'address':address,'tel':tel,'email':email})
    print(card)  

def update(card):
    name = input('수정할 데이터 이름 >>>')
    idx = -1
    for i, item in enumerate(card):
        if item['name'] == name:
            idx = i

            while True:
                update = input('수정할 정보-address,tel,email,exit(종료)>>> ')
                if update in ('address','tel','email'):
                    card[idx][update] = input(f'{update} 수정내용>>> ')
                elif update == 'exit':
                    break

            print(card[idx])
            break
    if idx == -1:
        print('등록되지 않은 데이터 입니다.')     

def delete(card):
    name = input('삭제할 이름 입력 >>>')
    delok = 0
    for i, item in enumerate(card):
        if item['name'] == name :
            print(item,'삭제!!')
            del card[i]
            delok = 1
            break
    if delok == 0:
        print('등록되지 않은 데이터 입니다.')

def cardlist(card):
    for item in card:
            print(f'''
----------------------------------------------
    이   름 : {item['name']}
    주   소 : {item['address']}
    전화번호 : {item['tel']}
    이 메 일 : {item['email']} ''')

def search(card):
    name = input('검색할 이름 >>>')
    idx = -1
    for i, item in enumerate(card):
        if item['name'] == name:
            idx = i
            print(item)
            break
    if idx == -1:
        print('등록되지 않은 데이터 입니다.')

def datasave(card):
    with open('01_basic/namecard.data','w') as f:
        card = json.dump(card,f)

def dataload(card):
    with open('01_basic/namecard.data','r') as f:
        card = json.load(f)
    return card
    
import cardfunc as cf
# card=[{'name':'홍길동', 'address':'서울', 'tel':'1111-1111-1111','email':'hong@gmail.com'},
#       {'name':'김나리', 'address':'광주','tel':'111-1111-1112','email':'kim@gmail.com'}]
card = []
card = cf.dataload(card)
while True:
    menu = input('''
--------------------------------------------------
1.저장  2.수정  3.삭제  4.리스트  5.검색  6.종료(Q)
--------------------------------------------------
>>>''')
    if menu == '1':
        cf.save(card) #def save()에서주소값이 넘어간다
        while True:

            name = input('이름을 입력하세요 >>>')
            check = 0
            for item in card:
                if item['name'] == name:
                    check = 1
            if check == 0:
                    break
            print('중복되는 이름이 있습니다.')
                
        address = input('주소를 입력하세요 >>>')
        tel = input('전화번호를 입력하세요 >>>')
        email = input('이메일을 입력하세요 >>>')
        card.append({'name':name,'address':address,'tel':tel,'email':email})
        print(card)  
        
    elif menu == '2': 
        cf.update(card)     
        name = input('수정할 데이터 이름 >>>')
        idx = -1
        for i, item in enumerate(card):
            if item['name'] == name:
                idx = i

                while True:
                    update = input('수정할 정보-address,tel,email,exit(종료)>>> ')
                    if update in ('address','tel','email'):
                        card[idx][update] = input(f'{update} 수정내용>>> ')
                    elif update == 'exit':
                        break

                print(card[idx])
                break
        if idx == -1:
            print('등록되지 않은 데이터 입니다.')     

    elif menu == '3':
        cf.delete(card)
        name = input('삭제할 이름 입력 >>>')
        delok = 0
        for i, item in enumerate(card):
            if item['name'] == name :
                print(item,'삭제!!')
                del card[i]
                delok = 1
                break
        if delok == 0:
            print('등록되지 않은 데이터 입니다.')

    elif menu == '4':
        cf.cardlist(card)
        for item in card:
            print(f'''
----------------------------------------------
    이   름 : {item['name']}
    주   소 : {item['address']}
    전화번호 : {item['tel']}
    이 메 일 : {item['email']} ''')

    elif menu == '5':
        cf.search(card)
        name = input('검색할 이름 >>>')
        idx = -1
        for i, item in enumerate(card):
            if item['name'] == name:
                idx = i
                print(item)
                break
        if idx == -1:
            print('등록되지 않은 데이터 입니다.')

    elif menu in ('6','q','Q'):
        print('프로그램 종료')
        break
    else:
        print('메뉴선택을 잘못하셨습니다.')

cf.datasave(card)





