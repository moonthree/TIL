sugar = int(input())

max_three = 5000 // 3
max_five = 1000

min_sugar = []

for i in range(max_three+1):
    for j in range(max_five+1):
        if (5 * j) + (3 * i) == sugar:
            min_sugar.append(j+i)

if min_sugar:
    print(min(min_sugar))
else:
    print(-1)