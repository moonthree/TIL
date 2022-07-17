#2058 자릿수 더하기

N = int(input())

sum = 0
sum += N // 1000
sum += N%1000 // 100
sum += N%1000%100 // 10
sum += N%1000%100%10
print(sum)
