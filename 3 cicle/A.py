N = int(input())
for i in range(0, N):
    print(i * 2 + 2, end=(' ' if i < (N - 1) else '\n'))