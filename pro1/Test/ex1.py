# 큰수의 법칙 - 제일큰수를 가장 많이 더해야 가장큰수가 됨
data = list(map(int, input('숫자 배열 넣을 값들 정하세요 띄어쓰기 구분').split()))
n = len(data) # 배열의크기
m,k = map(int, input('숫자입력 : 더하는횟수,연속몇번').split())

# print(n,m,k)

# n = 배열크기, m = 더해지는횟수, k 만큼 초과하여 더할순 없다. 즉   k-1이 최대횟수
# print(len(data))
# print(data)
data.sort()

one = data[n-1] # 첫번째로 큰값
two = data[n-2] # 두번째로 큰값

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += one
        m -= 1
    if m == 0:
        break
    result += two
    m -= 1
    
print(result)
    
        




