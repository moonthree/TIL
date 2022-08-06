# 최대공약수와 최소공배수

a, b = map(int, input().split())

def Euclidean(a, b):
    r = b % a
    if r == 0:
        return a
    return(Euclidean(r, a))

c = 0
if a > b:
    print(Euclidean(a, b))
    c = Euclidean(a, b)
    print(c*(a//c)*(b//c))
elif a < b:
    print(Euclidean(b, a))
    c = Euclidean(b, a)
    print(c*(a//c)*(b//c))
elif a == b:
    print(a)
    print(a)
