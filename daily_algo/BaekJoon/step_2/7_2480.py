a, b, c= map(int, input().split())

if a == b == c:
    print(10000+a*1000)
elif a == b or a == c:
    print(1000+a*100)
elif b == c:
    print(1000+b*100)
elif a != b != c:
    num_list = [a, b, c]
    num_max = max(num_list)
    print(num_max*100)