def sum_of_repeat_number(num):
    b = []
    for j in num:
        cnt = 0
        for i in num:
            if j == i:
                cnt += 1
        if cnt == 1:
            b.append(j)
    return print(sum(b))



sum_of_repeat_number([4, 4, 7, 8, 10, 4])