test_case = int(input())

for _ in range(test_case):
    H, W, N = map(int, input().split())

    room = N//H+1
    floor = N%H

    if floor == 0:
        floor = H
        room -= 1
    print(floor*100+room)


    #print(f'{floor}{room}')