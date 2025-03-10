import sys
t = int(input())

for i in range(t):
    a , b = map(int,sys.stdin.readline().split())
    result = a+b
    print("Case #",i+1,": ",result ,sep='')