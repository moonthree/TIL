sum = 0

for i in range(1, 1000):
    if i % 2 == 0:
        sum += i
    if i % 7 == 0:
        sum += i
    if i % 14 == 0:
        sum -= i

print(sum)
