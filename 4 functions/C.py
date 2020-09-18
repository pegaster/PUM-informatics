def mult_sum(N):
    mult = 1
    mult_list = [1]
    i = 2
    end = N // 2
    while i < end:
        if N % i == 0:
            end = N // i
            mult += i
            if end != i:
                mult += end
            mult_list.append(i)
        i += 1
    return mult

if __name__ == "__main__":
    nums = input().split()
    check = mult_sum(int(nums[0])) == int(nums[1]) and mult_sum(int(nums[1])) == int(nums[0])
    print('YES' if check else 'NO')