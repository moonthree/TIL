import mass_percent

n = 0
a = []

while n < 5:
    a.append(list(map(str, input('소금물의 농도와 양을 입력하세요: ').split())))
    if a[n][0] == 'Done':
        a.remove(a[n])
        break
    else:
        n += 1

print(mass_percent.salt_water(a))
