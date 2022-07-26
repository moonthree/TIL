def salt_water(a):
    salt = []
    salt_water = []
    for i in range(len(a)):
        salt.append(int(a[i][0])*int(a[i][1])/100)

    for i in range(len(a)):
        salt_water.append(int(a[i][1]))

    per = round(sum(salt)/sum(salt_water)*100, 2)
    water = round(sum(salt_water), 2)
    return f'{per}% {water}g'