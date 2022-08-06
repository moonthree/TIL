
while True:
    n = int(input())
    if n == 0 : break

    b = 2*n
    array = [True for i in range(b+1)]

    for i in range(2, int(b**0.5)+1):
        if array[i] == True:
            j = 2
            while i*j <= b:
                array[i * j] = False
                j += 1
    
    count = 0
    for i in range(n+1, b+1):
        if array[i]:
            count += 1
    print(count)