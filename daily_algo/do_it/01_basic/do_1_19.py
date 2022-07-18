# 1_19 start

# 1~12까지 8을 건너뛰고 출력하기 1

for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')

print()
'''
의도대로 실행 되자만 비효율적임 why?
숫자를 100,000까지 출력하며 딱 1개만 건너 뛴다고 가정할 시
판단을 10만 번 해야 함
'''
# 1_19 end


# 1_20 start

# 1~12까지 8을 건너뛰고 출력하기 2

for i in list(range(1, 8)) + list(range(9, 13)):
    print(i, end=' ')
print()

# 1_20 end