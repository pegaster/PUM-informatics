N = int(input())
l = list(map(int, input().split()))
for i in range(3):
    minimum = l[0]
    min_index = 0
    for j in range(1, len(l)):
        if l[j] < minimum:
            minimum = l[j]
            min_index = j
    l.pop(min_index)

    print(minimum, end=' ')
print('')