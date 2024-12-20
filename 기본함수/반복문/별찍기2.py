n = int(input())

for i in range(n):
    for j in range(n-(i+1)):
        print(" ",end="")
    for x in range(i+1):
        print("*", end="")
    print("")