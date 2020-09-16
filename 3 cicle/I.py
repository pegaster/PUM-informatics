def isSimple(num):
    for j in range(2, num):
        if num % j == 0:
            return False
    return True


nums = input().split()
start = int(nums[0])
end = int(nums[1])

result_list = []
for i in range(start, end+1):
    if i <= 2:
        result_list.append(i)
    else:
        if isSimple(i):
            result_list.append(i)

if result_list == []:
    print(0)
else:
    for item in result_list:
        print(f' {item}', end='')
