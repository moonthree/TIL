def fn_d(n):
    str_n = str(n)
    b = 0
    for i in range(len(str_n)):
        b += int(str_n[i])
    return b+n
print(fn_d(3))

def is_selfnumber(n):
    cnt = 0
    
    for i in range(1, n):
        if fn_d(i) == n:
            cnt += 1
    if cnt == 0:
        return 'self'
    else :
        return 'not self'
print(is_selfnumber(31))