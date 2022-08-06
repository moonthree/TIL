n = int(input())

big_list = []
cnt = 0
while n != cnt:
    a, b = map(int, input().split())
    big_list.append([a, b])
    cnt += 1

rank = []
for i in range(n):
    rank = 1
    for j in range(n):
        if big_list[i][0] < big_list[j][0] and big_list[i][1] < big_list[j][1]:
            rank += 1
    print(rank, end=" ")