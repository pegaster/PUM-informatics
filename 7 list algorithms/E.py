N = int(input())
l = list(map(int, input().split()))
check = l[0]
check_of_count_max = l[0]
count = 1
count_max = 1
for i in range(1, N):
    if l[i] == check:
        count +=1
        if count_max < count:
            count_max = count
            if check_of_count_max != check:
                check_of_count_max = check
    else:
        check = l[i]
        count = 1
print(check_of_count_max, count_max)