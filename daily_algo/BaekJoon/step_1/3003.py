piece = list(map(int, input().split()))

correct = [1, 1, 2, 2, 2, 8]

work = []
for i in range(len(piece)):
    work.append(correct[i] - piece[i])

for i in work:
    print(i, end=' ')