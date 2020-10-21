nums = input().split()
for i in range(len(nums)):
    nums[i] = int(nums[i])
maximum = nums[0]
max_index = 0
for i in range(1, len(nums)):
    if nums[i] > maximum:
        maximum = nums[i]
        max_index = i
print(maximum, max_index)