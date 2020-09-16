import random
nums = input().split()
for i in range(4):
    print('{:.3f}'.format(random.uniform(float(nums[0]), float(nums[1]) - 0.001)), end=' ')
print('{:.3f}'.format(random.uniform(float(nums[0]), float(nums[1]) - 0.001)))