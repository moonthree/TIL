# def sum_digit(number):
#     if number < 10:
#         return number;
#     return (number % 10) + sum_digit(number // 10) 


# for j in range(1, 100):
#     cnt = 0
#     self_number = []
#     for k in range(1, j):
#         m = sum_digit(k)+k

#         if m == j:
#             cnt += 1
#             break
#     if cnt == 0:
#         print(j)

num = set(range(1, 10001))
new_num = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    new_num.add(i)

self_num = sorted(num - new_num)
for i in self_num:
    print(i)