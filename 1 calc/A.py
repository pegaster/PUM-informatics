nums = input().split()
sum_result = 0
mult_result = 1

for num in nums:
    sum_result += int(num)
    mult_result *= int(num)

for i in range(len(nums)):
    if i == 0:
        print(nums[i], end='')
    else:
        print('+' + nums[i], end='')
        if i == len(nums) - 1:
            print('=' + str(sum_result))

for i in range(len(nums)):
    if i == 0:
        print(nums[i], end='')
    else:
        print('*' + nums[i], end='')
        if i == len(nums) - 1:
            print('=' + str(mult_result)) 

for i in range(len(nums)):
    if i == 0:
        print('(' + nums[i], end='')
    else:
        print('+' + nums[i], end='')
        if i == len(nums) - 1:
            print(')/' + str(len(nums)) + '=' + '{:.3f}'.format(sum_result/3))

