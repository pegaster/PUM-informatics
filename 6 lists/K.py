N, K = [int(s) for s in input().split()]
row = ['I' for i in range(N)]
for i in range(K):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        row[j] = '.'
for i in row:
    print(i, end='')