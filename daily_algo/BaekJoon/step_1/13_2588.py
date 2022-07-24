a = int(input())
b = int(input())

c = str(b)
for i in range(2, -1, -1):
    print(a*int(c[i])) 

print(a*b)
