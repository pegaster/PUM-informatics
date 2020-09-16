def bool_to_int(bool):
    if bool:
        return 1
    else:
        return 0

if __name__ == "__main__":
    nums = input().split(' ')
    result = bool_to_int(int(nums[0]) == int(nums[1])) + bool_to_int(int(nums[1]) == int(nums[2])) + bool_to_int(int(nums[0]) == int(nums[2]))
    if result == 1:
        result += 1
    print(result)
