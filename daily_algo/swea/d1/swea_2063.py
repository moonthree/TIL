#2063 중간값 찾기

N = int(input())
score = sorted(list(map(int, input().split())))
print(score[N//2])