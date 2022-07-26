t = int(input())

for i in range(t):
    b = []
    cnt = 0
    ox = input()
    for j in range(len(ox)):
        if ox[j] == 'O':
            b.append('O')
            cnt += len(b)
        elif ox[j] == 'X':
            b = []
    print(cnt)