import random
nums = input().split()
for i in range(4):
    print(random.randint(int(nums[0]), int(nums[1])), end=' ')
print(random.randint(int(nums[0]), int(nums[1])))