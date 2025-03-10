# t = int(input())
# n = str(input())
# result = 0

# for i in range(t):
#     result += int(n[i])

# print(result)
# 리스트 함수 이용
t = int(input())
n = list(map(int,input()))
print(sum(n))