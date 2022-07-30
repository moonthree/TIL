test_case = int(input())

for _ in range(test_case):
    num, letter = map(str, input().split())
    for i in letter:
        print(i*int(num), end='')
    print()