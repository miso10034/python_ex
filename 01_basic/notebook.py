class Note:
    def __init__(self,contents=None): #내용을 넣어도 되고 안넣어도 된다.
        self.contents = contents

    def write_contents(self, contents): #컨텐츠 쪽에 파라미터를 받는다.
        self.contents = contents

    def remove_all(self):
        self.contents = ''

    def __str__ (self):#인스턴트를 찍을 때 나타나는 개체
        if self.contents == None:
            self.contents = '없음'
        return self.contents


note01 = Note()
print(note01)
note02 = Note('파이썬 프로그래밍!!!')
print(note02)
note01.write_contents('추가내용 입력!!!')
print(note01)
note01.remove_all()
print(note01)

class NoteBook:
    def __init__(self,title):
        self.title = title #지역변수
        self.page_number = 1 #첫번째 페이지를 디폴트로
        self.notes = {}

    def add_note(self,note,page=0):
        if self.page_number < 300:
            if page == 0:
                self.notes[self.page_number] = note #[]
                self.page_number += 1 # 값이 들어갔으니 1을 추가
            else:
                self.notes = {page:note} # 값이 들어오지않았으면
                self.page_number += 1
        else:
            print('페이지가 모두 채워졌습니다.')

def remove_note(self,page_number): #ㅈㅣ우고자하는 페이지 넘버를 입력받아 지운다.
    if page_number in self.notes.keys(): #지우려고하는 페이지가 있는지 확인
        return self.notes.pop(page_number) #해당페이지는 팝으로 꺼내서 삭제한다.
    else: #못찾았으면
        print('해당 페이지는 존재하지 않습니다.')

def get_number_of_pages(self):
    return len(self.notes.keys())#실제있는 페이지에 키값만 받아서 반환한다.