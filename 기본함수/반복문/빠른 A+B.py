import sys
t = int(sys.stdin.readline())

## 2차원 리스트로 입력받기 [1],[2],[3],[4]
for i in range(t):
    a , b = map(int,sys.stdin.readline().split())
    print(a+b)
