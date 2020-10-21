import random
a, b, n = map(int, input().split())
l = [random.randint(a, b) for i in range(n)]
min_sum = l[0] + l[1]
index1 = 0
index2 = 1
for i in range(2, len(l) - 1):
    if l[i] + l[i + 1] <= min_sum:
        min_sum = l[i] + l[i + 1]
        index1 = i
        index2 = i + 1
for i in l:
    print(i, end=' ')
print('')

print(index1 + 1, index2 + 1)