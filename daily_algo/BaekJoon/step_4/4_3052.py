n = 0
nums = []
while n < 10:
    nums.append(int(input()))
    n += 1

remain = []
for i in nums:
    remain.append(i % 42)

print(len(set(remain)))