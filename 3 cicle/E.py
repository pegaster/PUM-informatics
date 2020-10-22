nums = input().split()
a = int(nums[0])
b = int(nums[1])

count = 0

while (a != 0) and (b != 0):
    if a > b:
        a -= b
    else:
        b -= a
    count += 1
print(b if a == 0 else a, end=' ')
print(count)