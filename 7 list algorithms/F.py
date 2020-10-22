N = int(input())
l = input().split()
for i in range(N // 2):
    l[i], l[N - i - 1] = l[N - i - 1], l[i]
print(' '.join(l))
