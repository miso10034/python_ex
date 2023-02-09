# # import json
# # def save(card):
# #     while True:
# #         booknumber = input('일련번호를 입력하세요 >>>')
# #         check = 0
# #         for item in card:
# #             if item['booknumber'] == booknumber:
# #                 check = 1
# #         if check == 0:
# #                 break
# #         print('중복되는 일련번호가 있습니다.')

# #     bookname = input('c책이름을 입력하세요 >>>')
# #     bookoriented = input('출판사를 입력하세요 >>>')
# #     card.append({'booknumber':booknumber,'bookname':bookname,'bookoriented':bookoriented})
# #     print(card)

# # def update(card):
# #     booknumber = input('수정할 책일련번호 >>>')
# #     idx = -1
# #     for i, item in enumerate(card):
# #         if item['booknumber'] == booknumber:
# #             idx = i
          
# #             while True:
# #                 update =input('수정할 정보-booknumber,bookname,bookoriented,exit(종료)>>> ')
# #                 if update in ('booknumber','bookname','bookoriented'):
# #                     card[idx][update] = input(f'{update} 수정내용>>> ')
# #                 elif update == 'exit':
# #                     break

# #             print(card[idx])
# #             break
# #     if idx == -1:
# #         print('등록되지 않은 데이터 입니다.')

# # def delete(card):
# #     bookname = input('삭제할 책이름 입력 >>>')
# #     delk = 0
# #     for i, item in enumerate(card):
# #         if item['bookname'] == bookname:
# #             print(item, '삭제한다!')
# #             del card[i]
# #             delk = 1
# #             break
# #     if delk == 0:
# #         print('등록되지 않은 데이터 입니다.')

# # def cardlist(card):
# #     for item in card:
# #             print (f'''
# # ------------------------------------------------
# #     일 련 번 호 : {item['booknumber']}
# #     책   이  름 : {item['bookname']}
# #     출   판  사 : {item['bookoriented']}''' )

# # def search(card):
# #     bookname = input('검색할 책 이름 >>>')
# #     idx = -1
# #     for i, item in enumerate(card):
# #         if item['bookname'] == bookname:
# #             idx = i
# #             print(item)
# #             break
# #     if idx == -1:
# #         print('등록되지 않은 데이터 입니다.')

# # def datasave(card):
# #     with open('01_basic/namecard.data','w') as f:
# #         card = json.dump(f)

# # def dataload(card):
# #     with open('01_basic/namecard.data','r') as f:
# #         card = json.load(f)
# #     return card

# import cardfunc as cf
# #card=[['17890', 'c언어 정복하기','한빛'],
# #     ['67890','파이썬을 잡아라','아카데미']]
# card = []
# card = cf.dataload(card)
# while True:
#     menu = input('''
# ----------------------------------------------------
# 1.저장  2.수정  3.삭제  4.리스트  5.검색  6.종료(Q)
# ----------------------------------------------------
# >>>''')
#     if menu == '1':
#         cf.save(card)
#         while True:

#             booknumber = input('일련번호를 입력하세요 >>>')
#             check = 0
#             for item in card:
#                 if item['booknumber'] == booknumber:
#                     check = 1
#             if check == 0:
#                         break
#             print('중복되는 일련번호가 있습니다.')

#         bookname = input('c책이름을 입력하세요 >>>')
#         bookoriented = input('출판사를 입력하세요 >>>')
#         card.append({'booknumber':booknumber,'bookname':bookname,'bookoriented':bookoriented})
#         print(card)

#     elif menu == '2':
#         cf.update(card)
#         booknumber = input('수정할 책일련번호 >>>')
#         idx = -1
#         for i, item in enumerate(card):
#             if item['booknumber'] == booknumber:
#                 idx = i

#                 while True:
#                     update = input('수정할 정보-address,tel,email,exit(종료)>>> ')
#                     if update in ('address','tel','email'):
#                         card[idx][update] = input(f'{update} 수정내용>>> ')
#                     elif update == 'exit':
#                         break
                
#                 print(card[idx])
#                 break
#         if idx == -1:
#             print('등록되지 않은 데이터 입니다.')
            
#     elif menu == '3':
#         cf.delete(card)
#         bookname = input('삭제할 책이름 입력 >>>')
#         delk = 0
#         for i, item in enumerate(card):
#             if item['bookname'] == bookname:
#                 print(item, '삭제한다!')
#                 del card[i]
#                 delk = 1
#                 break
#         if delk == 0:
#             print('등록되지 않은 데이터 입니다.')

#     elif menu == '4':
#         cf.cardlist(card)
#         for item in card:
#             print (f'''
# ------------------------------------------------
#     일 련 번 호 : {item['booknumber']}
#     책   이  름 : {item['bookname']}
#     출   판  사 : {item[bookoriented]}''' )

#     elif menu == '5':
#         cf.search(card)
#         bookname = input('검색할 책 이름 >>>')
#         idx = -1
#         for i, item in enumerate(card):
#             if item['bookname'] == bookname:
#                 idx = i
#                 print(item)
#                 break
#         if idx == -1:
#             print('등록되지 않은 데이터 입니다.')

#     elif menu in ('6','q','Q'):
#         print('프로그램 종료')
#         break
#     else:
#         print('메뉴선택을 잘못하셨습니다.')

# cf.datasave(card)