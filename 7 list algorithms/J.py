def isFib(n):
    a = 0
    b = 1
    while a < n:
        a, b = a + b, a
    return a == n

N = int(input())
l = list(map(int, input().split()))
isPrinted = False
for i in l:
    if isFib(i):
        print(i, end=' ')
        isPrinted = True
print('' if isPrinted else '0')