A, B = map(str, input().split())

reverse_a = int(A[::-1])
reverse_b = int(B[::-1])

if reverse_a > reverse_b:
    print(reverse_a)
else:
    print(reverse_b)