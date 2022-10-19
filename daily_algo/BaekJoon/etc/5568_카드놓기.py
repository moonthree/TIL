n = int(input())
k = int(input())
arr = []
for _ in range(n):
    number = int(input())
    arr.append(number)
path = []
used = [0]*len(arr)
result = []
def rcr(level):

    if level == k:
        a = ''
        print(path)
        for i in path:
            a += str(i)
        if int(a) not in result:
            result.append(int(a))
        return

    for i in range(len(arr)):
        if used[i] == 0:
            used[i] = 1
            path.append(arr[i])
            rcr(level+1)
            path.pop()
            used[i] = 0

rcr(0)

print(len(result))