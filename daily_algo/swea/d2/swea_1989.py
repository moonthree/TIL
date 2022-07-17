#1989 초심자의 회문 검사

a = int(input())

for i in range(1, a+1):
    str = input()
    temp = ''
    for j in range(len(str)-1, -1, -1):
        temp += str[j]
    
    if str == temp:
        print('#%d %d' % (i, 1))
    else :
        print('#%d %d' % (i, 0))