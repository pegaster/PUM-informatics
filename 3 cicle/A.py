N = int(input())
for i in range(2, 2 * N + 2, 2):
    print(i, end=(' ' if i < (2 * N) else '\n'))