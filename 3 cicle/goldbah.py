def isSimple(num):
    for j in range(2, num):
        if num % j == 0:
            return False
    return True

N = int(input())
a = 0
b = 0

for i in range(2, N):
        if isSimple(i) and isSimple(N - i) and a != 1 and b != 1:
            a = i
            b = N - i
            break

print(f'{a} {b}')