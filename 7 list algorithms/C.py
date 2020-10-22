N = int(input())
l = list(map(int, input().split()))
minimum = l[0]
index_list = ['1']
for i in range(1, N):
    if minimum > l[i]:
        minimum = l[i]
        index_list = [str(i + 1)]
    elif minimum == l[i]:
        index_list.append(str(i + 1))
print(' '.join(index_list))
