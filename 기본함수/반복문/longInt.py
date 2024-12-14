n = int(input())
a = int(n/4)
talk = ""
long = "long "

for i in range(a):
    talk += long

print(talk + "int")