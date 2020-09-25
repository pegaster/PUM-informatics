def num_sum(num):
    result = 0
    while (num != 0):
        result = result + num % 10
        num = num // 10
    return result

def mult_check(number):
    current_num_sum = num_sum(number)
    result = True
    for i in range(2, 9 + 1):
        if num_sum(number * i) != current_num_sum:
            result = False
    return result

if __name__ == "__main__":
    nums = input().split()
    isPrinted = False
    for num in range(int(nums[0]), int(nums[1]) + 1):
        if mult_check(num):
            print(' ' if isPrinted else '', end='')
            print(num, end='')
            isPrinted = True
    print('' if isPrinted else 0)
