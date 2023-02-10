class Card:
    def __init__(self,bookname,booknumber,bookoriented):
        self.bookname = bookname
        self.booknumber = booknumber
        self.bookoriented = bookoriented
       
    def add_card(self,bookname,booknumber,bookoriented):
        self.bookname = bookname
        self.booknumber = booknumber
        self.bookoriented = bookoriented

    def remove_all(self):
        self.bookname = ''
        self.booknumber = ''
        self.bookoriented = ''

    def __str__(self):
        return f'bookname: {self.bookname}, booknumber: {self.booknumber}, bookoriented: {self.bookoriented}'

class BookCard:
    def __init__(self,title):
        self.title = title
        self.b_name = 1
        self.cards = {}

    # def add_card(self,b_name=0):
    #     if self.b_name == 0:
    #         self.cards[self.b_name] = card
    #         self.b_name += 1
    #     else:
            
    def remove_card(self.)