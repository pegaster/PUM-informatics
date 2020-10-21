import random
a, b, n = map(int, input().split())
l = [random.randint(a, b) for i in range(n)]
min_sum = l[0] + l[1]
index1 = 0
index2 = 1
print(l[0], l[1], end=' ')
for i in range(2, len(l) - 1):
    print(l[i], end=' ')
    if l[i] + l[i + 1] <= min_sum:
        min_sum = l[i] + l[i + 1]
        index1 = i
print(l[len(l) - 1])

print(index1 + 1, index1 + 2)