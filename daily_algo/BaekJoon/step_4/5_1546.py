n = int(input())

score = list(map(int, input().split()))
max_score = max(score)

new_score = []
for i in score:
    new_score.append(i/max_score*100)

new_score_avg = sum(new_score)/len(new_score)
print(new_score_avg)