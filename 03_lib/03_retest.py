#정규표현식
import re #내장함수 아니기 때문에 import필요

data = """
park 800905-1049118
kim  700905-1059119
"""

# pat = re.compile("(\d{6})[-]\d{7}") 
# #\d숫자를 의미 6번 반복 = 숫자가 6개 온다 []하나의 자릿수
# #앞에 숫자 여섯개 뒤에숫자 7개
# print(pat.sub("\g<1>-*******",data))# 이러한 패턴을 찾아 sub = 바꾸기
# #맨첫번째 그룹 갖고 와서 이걸로 바꿔라 ,data에서 찾아서 바꿔라

# p = re.compile('ab*')# ab조합 0회 이상
# print(p.match('cabb')) #match는 무조건 첫글자부터 비교
# print(p.search('cab')) #0의자리가 c 그래서 첫번째자리수부터 4번쨰자리까지 서치
# p = re.compile('[a-z]+')
# print(p.match('1asxr한'))
# print(p.search('1asxr한'))
# result = p.search('1asxr한')
# print(result)
# print(result.start())
# print(result.end())
# print(result.span())
# print(result.group())
# print(result.groups())

p = re.compile('[0-9]{6}[-][1-4][0-9]{6}')
result = p.findall(data)
print(result)
for r in result: print(r)

p = re.compile('[0-9]{6}[-][1-4][0-9]{6}')
result = p.finditer(data)
print(result)
for r in result: print(r)
