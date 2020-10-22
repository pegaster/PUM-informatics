N = int(input())
l = list(map(int, input().split()))
maximum = l[0]
count = 1
for i in range(1, N):
    if l[i] == maximum:
        count += 1
    elif l[i] > maximum:
        maximum = l[i]
        count = 1
print(maximum, count)