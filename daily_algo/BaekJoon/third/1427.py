n = int(input())

a = str(n)

list_a = []
for i in a:
    list_a.append(int(i))

list_a.sort(reverse=True)

for i in list_a:
    print(i, end='')
