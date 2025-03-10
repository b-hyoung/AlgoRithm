# n = int(input())

# for i in range(n):
#     for j in range(n-(i+1)):
#         print(" ",end="")
#     for x in range(i+1):
#         print("*", end="")
#     print("")
n = int(input())
star = "*"
for i in range(n):
    index = i+1
    idx= n-index
    if(index-n < 0):
        print(" "*idx,end= "")
    print("*"*index)