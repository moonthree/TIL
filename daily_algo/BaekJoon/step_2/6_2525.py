A, B = map(int, input().split())
C = int(input())

total = A*60 + B + C
hour = 0
minute = 0

if total//60 >= 24:
    hour = total//60 - 24
    minute = int(total%60)
else :
    hour = total//60
    minute = int(total%60)

print(hour, minute)