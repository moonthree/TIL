C = int(input())
for i in range(C):
    score = list(map(int, input().split()))

    total_score = sum(score)-score[0]
    avg = total_score/score[0]

    cnt = 0
    for i in range(1, len(score)):
        if score[i] > avg:
            cnt += 1
    
    a = round(cnt/score[0]*100, 3)
    print(f'{a:.3f}%')