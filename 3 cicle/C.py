nums = input().split()
start = int(nums[0])
end = int(nums[1]) + 1
isPrinted = False

for num in range(start, end):
    place = []
    for j in range(len(str(num))):
        place.append(int(str(num)[j]))
    asum = 0
    for i in place:
        asum += i ** len(place)

    if num == asum:
        print((' ' if isPrinted else '') + str(num), end='')
        isPrinted = True

print('' if isPrinted else '-1', end='')
