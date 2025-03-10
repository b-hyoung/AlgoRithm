# n = int(input())
# str = "*"

# for i in range(n):
#     print(str*(i+1))
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print("\n",end="")