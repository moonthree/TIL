from copy import deepcopy

N = int(input())
arr = [[0]*N for _ in range(N)]

def visit(y, x):
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(8):
        for j in range(1, N):
            ny = y + dy[i] * j
            nx = x + dx[i] * j
            if 0 <= ny < N and 0 <= nx < N:
                if arr[ny][nx] == 1: continue
                arr[ny][nx] = 1

cnt = 0
def dfs(level, yst, xst):
    global cnt, arr
    if level == N:
        cnt += 1
        return
    for y in range(yst, N):
        for x in range(xst, N):
            if arr[y][x] == 1: continue
            backup = deepcopy(arr)
            arr[y][x] = 1
            visit(y, x)
            arr = deepcopy(backup)

dfs(0, 0, 0)
print(cnt)