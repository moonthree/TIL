n = 0
a = []
while n < 9:
    b = int(input())
    a.append(b)
    n += 1
big = max(a)
idx = a.index(big) + 1
print(big)
print(idx)
