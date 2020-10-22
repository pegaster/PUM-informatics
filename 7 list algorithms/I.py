def IsPrime(num):
    for j in range(2, num):
        if num % j == 0:
            return False
    return i > 1
N = int(input())
l = list(map(int, input().split()))
isPrinted = False
for i in l:
    if IsPrime(i):
        print(i, end=' ')
        isPrinted = True
print('0' if not isPrinted else '')
        