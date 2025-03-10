sum = 0
all= int(input())
n = int(input())
for i in range(n):
    a ,b = map(int,input().split())
    x = a*b
    sum += x

if(all == sum):
    print("Yes")
else:
    print("No")