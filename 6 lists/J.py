nums1 = input().split()
zero_count = 0
for i in nums1:
    if i == '0':
        zero_count += 1
    else:
        print(i, end=' ')
for i in range(zero_count):
    print(0, end=' ')
print('')