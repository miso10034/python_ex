import json
def save(card):
    while True:
        booknumber = input('일련번호를 입력하세요 >>>')
        check = 0
        for item in card:
            if item['booknumber'] == booknumber:
                check = 1
        if check == 0:
                break
        print('중복되는 일련번호가 있습니다.')

    bookname = input('c책이름을 입력하세요 >>>')
    bookoriented = input('출판사를 입력하세요 >>>')
    card.append({'booknumber':booknumber,'bookname':bookname,'bookoriented':bookoriented})
    print(card)

def update(card):
    booknumber = input('수정할 책일련번호 >>>')
    idx = -1
    for i, item in enumerate(card):
        if item['booknumber'] == booknumber:
            idx = i
          
            while True:
                update =input('수정할 정보-booknumber,bookname,bookoriented,exit(종료)>>> ')
                if update in ('booknumber','bookname','bookoriented'):
                    card[idx][update] = input(f'{update} 수정내용>>> ')
                elif update == 'exit':
                    break

            print(card[idx])
            break
    if idx == -1:
        print('등록되지 않은 데이터 입니다.')

def delete(card):
    bookname = input('삭제할 책이름 입력 >>>')
    delk = 0
    for i, item in enumerate(card):
        if item['bookname'] == bookname:
            print(item, '삭제한다!')
            del card[i]
            delk = 1
            break
    if delk == 0:
        print('등록되지 않은 데이터 입니다.')

def cardlist(card):
    for item in card:
            print (f'''
------------------------------------------------
    일 련 번 호 : {item['booknumber']}
    책   이  름 : {item['bookname']}
    출   판  사 : {item['bookoriented']}''' )

def search(card):
    bookname = input('검색할 책 이름 >>>')
    idx = -1
    for i, item in enumerate(card):
        if item['bookname'] == bookname:
            idx = i
            print(item)
            break
    if idx == -1:
        print('등록되지 않은 데이터 입니다.')

def datasave(card):
    with open('01_basic/namecard.data','w') as f:
        card = json.dump(f)

def dataload(card):
    with open('01_basic/namecard.data','r') as f:
        card = json.load(f)
    return card
