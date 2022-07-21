A = int(input())
B = int(input())
C = int(input())

D = A*B*C
E = []
for i in map(int, str(D)):
    E.append(i)

n = 0
while n<10: 
    s = 0
    for i in range(len(E)):
        if E[i] == n:
            s += 1
    n += 1
    print(s)