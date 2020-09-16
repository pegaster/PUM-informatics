n = int(input())
prev1 = 1
prev2 = 1
for i in range(0, n):
    if i <= 1:
        print('1', end=' ')
    else:
        print(prev1 + prev2, end=' ')
        if i % 2 == 0:
            prev1 += prev2
        else:
            prev2 += prev1
print('')


