N = int(input())
l1 = input().split()
l2 = []
r = (N - int(input()))
for i in range(N):
    l2.append(l1[i - r])
print(' '.join(l2))
