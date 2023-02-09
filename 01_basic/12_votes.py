'''
반장 선거에서 투표한 후보자 번호들을 공백을 구분자로 하여 입력하면
각 값들을 분리하고, 분리한 값들은 숫자로 변경하여
각 숫자별로 같은 값의 개수를 체크하여 출력해준다.
함수는 아래와 같이 작성한다.
- 공백을 구분자로 하여 입력받은 후보자 번호를 분리하는 함수
- 숫자로 변경된 값들의 항목별로 개수를 카운트하는 함수
- 결과값을 출력하는 함수
'''

def str2int(votes):
    result = votes.split()
    # for i, item in enumerate(result):
    #     result[i] = int(item)
    result = list(map(int,result))# 들어온 값을 쪼개고 숫자로 바꾸고 리스트로 만든다음 리턴했다.
    return result

def countvotes(votes):
    n = max(votes)
    result =[ 0 for i in range(n)] #4개의 공간 만들어주고 초깃값은 0
    # for i in range(n):
    #    result.append(0)

    for item in votes:
        result[item-1] += 1 #item-1는 첫번째 자리
    return result

def printresult(result):
    for i,count in enumerate(result): # i는 인덱스
        print(f'기호 : {i+1 :2} 득표수 : {count}')

votes = input("투표데이터 >>> ") # 1 2 2 3 4 5 3 2 4
result = str2int(votes)
print(result)   # [1,2,2,3,4,5,3,2,4]

result = countvotes(result)
print(result)
printresult(result)
