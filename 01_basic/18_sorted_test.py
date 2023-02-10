# 리스트에 저장된 데이터 정렬
data = [
    ['홍길동','A',22],
    ['박정인','C',31],
    ['김철수','B',16],
    ['홍인경','C',23]
]
#sotr는 원본에 바로 적용되어 정렬이 된다.
#data.sort(reverse=False,key=lambda x:(x[1],x[2])) #나이가 적은순부터 많은 순으로 정렬되었다.

# data.sort(reverse=False,key=lambda x:(x[1],-x[2]))
# print(data)

# result = sorted(data,key=lambda x:(x[1],x[2]))
# print(data)
# print(result)

#딕셔너리는 sort()가 없어서 sorted() 사용
#원본에 손을 안내고 결과값을 만들어내서 리턴한다.


# 딕셔너리에 저장된 데이터
data = [
    {'name':'홍길동','score':'A','age':22},
    {'name':'박정인','score':'C','age':31},
    {'name':'김철수','score':'B','age':16},
    {'name':'홍인경','score':'C','age':23}
]

# data.sort()
result = sorted(data,key=lambda x:(x[1]))
print(result)



# 클래스에 저장된 데이터 정렬

