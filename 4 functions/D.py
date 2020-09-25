import math
def mult_sum(N):
    mult = 1
    i = 2
    end = math.ceil((N) ** 0.5)
    while i < end:
        if N % i == 0:
            mult += i
            if (N // i) != i:
                mult += N // i
        i += 1
    return mult


if __name__ == "__main__":
    isPrinted = False
    nums = input().split()
    for i in range(int(nums[0]), int(nums[1]) + 1):
        if mult_sum(mult_sum(i)) == i and mult_sum(i) > i and int(nums[0]) < mult_sum(i) <= int(nums[1]):
            print((' ' if isPrinted else ''), end='')
            print(f'({i},{mult_sum(i)})', end='')
            isPrinted = True
    print('' if isPrinted else 0)
