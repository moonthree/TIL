from os import remove


def lonely(nums):
    lonely_nums = []
    for i in range(len(nums)-1):
        if nums[i] != nums[i+1]:
            lonely_nums.append(nums[i])
    if nums[-1] == nums[-2]:
        lonely_nums.append(nums[-1])
    return lonely_nums

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))