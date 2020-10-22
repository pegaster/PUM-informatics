N = int(input())
l = input().split()

left = 0
right = N - 1
while left <= right:
    for i in range(left, right, +1):
        if (l[i])[-1] > (l[i + 1])[-1]:
            l[i], l[i + 1] = l[i + 1], l[i]

    right -= 1
    for i in range(right, left, -1):
        if (l[i - 1])[-1] > (l[i])[-1]:
            l[i], l[i - 1] = l[i - 1], l[i]
    left += 1


print(' '.join(l))