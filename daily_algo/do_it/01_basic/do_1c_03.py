# 2자리 양수 입력 받기

print('2자리 양수를 입력하세요.')

while True:
    no = int(input('값을 입력하세요. : '))
    if no < 10 or no > 99:
        print('2자리 양수를 입력하세요.')
    if no >= 10 and no <= 99:
        break