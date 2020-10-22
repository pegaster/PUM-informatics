N = int(input())
l = list(map(int, input().split()))

for i in range(N - 1): 
        for j in range(N - i - 1): 
            if l[j] > l[j + 1] : 
                l[j], l[j + 1] = l[j + 1], l[j]

for i in l:
    print(i, end=' ')
 
print('')
print(len(set(l)))