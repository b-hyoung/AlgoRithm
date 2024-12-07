h , m = map(int,input().split())
a , b = 0 , 0
if(m - 45 < 0):
    a = m + 15
    if(h - 1 < 0):
        b = 23
    else:
        b = h - 1
elif(m - 45 >= 0):
    a = m - 45
    b = h

print(b,a)