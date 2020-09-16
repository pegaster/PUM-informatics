nums = input().split(' ')
for i in range(len(nums)):
    nums[i] = int(nums[i])
# bubble sort
for i in range(len(nums)):
    for j in range(0, len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            buffer = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = buffer
print(str(nums[0]) + '\n' + str(nums[-1]))
