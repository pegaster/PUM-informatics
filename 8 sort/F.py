N = int(input())
l = list(map(int, input().split()))

if N == 1:
    print(l[0])

for i in range(N - 1):
    flag = True 
    for j in range(N - 1, i, -1): 
        if l[j] < l[j - 1]:
            l[j], l[j - 1] = l[j - 1], l[j]
            flag = False

    if flag:
        continue
    print(' '.join(list(map(str, l))))