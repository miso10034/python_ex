class Card: #명함 한장애 대한 기능에 대한 클래스
    def __init__(self,name,address,tel,email): #지역변수 
        self.name = name #클래스 안에서 인스턴스별로 각 데이터마다 따로 값을 갖게 한다.sel. 형태
        self.address = address #오른쪽에서 왼쪽에 값을 넣어줌
        self.tel = tel #17_namecard의 35번째줄 생성시 __init__ 실행
        self.email = email

    def wirte_card(self,name,address,tel,email):
        self.name = name
        self.address = address
        self.tel = tel
        self.email = email

    def remove_all(self):
        self.name ='' # 
        self.address =''
        self.tel = ''
        self.email = ''

    def __str__(self): # 17네임카드의 45번쨰줄 print(card)의 호출에 의해서 이게 str형태로 리턴
        return f'name: {self.name}, address:{self.address}, tel:{self.tel}, email:{self.email}'
                # 반환되는 값들의 형식 형태를 바꿔서도 가능 
class CardBook: #명함을 여러장 가질수 있는 공간을 관리하는 클래스
    def __init__(self,title):
        self.title = title #제목 명함집을 여러개 만들어서 쓸수도 있따.제목이란걸 값으로 가진다.
        self.page_number = 1 #키값으로 접근하는 형태 300페이지가 되는 명함여러장에 접근 1부터 시작하고 점점 증가하는 형태
        self.cards = {} #명함에 대한 정보가 클래스 안에 있는 딕셔너리에 저장이 된다.

    def add_card(self,card,page=0): #
        if self.page_number < 300: #내가 가진 페이지수를 확인해서 300보다 작으면 값을 넣어준다.
            if page == 0:# 페이지가 비어 있으면
                self.cards[self.page_number] =card 
                self.page_number += 1
            else:
                self.cards = {page:card} #페이지값을 직접 받으면  키를 페이지라고 하고 card를 값으로 
                self.page_number += 1
        else:
            print('페이지가 모두 채워졌습니다.') # 300넘으면 실행

    def remove_card(self, page_number):
        if page_number in self.cards.keys(): #페이지 넘버를 가지고키값이 뭐가 있는지
            return self.cards.pop(page_number)
        else:
            print('해당 페이지는 존재하지 않습니다.')

    def get_number_of_pages(self): # 페이지수를 확인하는 함수
        return len(self.cards.keys())

    def list_cards(self,key= None,reverse =False): #list card는 전체명함
        if key==None:
            for page in self.cards:
                print(self.cards[page])    
        else:                                                                   #카드클래스가 갖고 있는 속성중에서 키값으로 들어오는 것에 따라 실행
            sorted_dict = sorted(self.cards.items(), key = eval(f'lambda item: item[1].{key}'), reverse =reverse)
            for page,card in sorted_dict: #sorted(self.cards.items()이렇게 하면 튜플만 [(),()] #람다 다음에 아이템에 튜플로 들어옴 뒷쪽에 있는 카드클래스를 리턴
                print(card) #sorted_dict는 대괄호로 결과값을 뽑아낸다 언팩킹형태로
                #__str__실행