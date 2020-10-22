N = int(input())
l = list(map(int, input().split()))
k = int(input())
left = 0
right = N - 1
while left <= right:
    for i in range(left, right, +1):
        if l[i] > l[i + 1]:
            l[i], l[i + 1] = l[i + 1], l[i]

    right -= 1
    for i in range(right, left, -1):
        if l[i - 1] > l[i]:
            l[i], l[i - 1] = l[i - 1], l[i]
    left += 1

check = l[0]

count = 1
isPrinted = False
for i in range(1, N):
    if l[i] == check:
        count += 1
    else:
        if count == k:
            print(check, end=' ')
            isPrinted = True
        check = l[i]
        count = 1

print('' if isPrinted else '0')