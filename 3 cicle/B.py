nums = input().split()
start = int(nums[0])
end = int(nums[1]) + 1

for i in range(start, end):
    print(f'{i}*{i}={i ** 2}')
