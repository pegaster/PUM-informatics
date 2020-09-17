N = int(input())
mult = 0
mult_list = []
end = N // 2
for i in range(1, end + 1):
    if N % i == 0:
        if mult == 0:
            end = N / i
        mult += i
        mult_list.append(i)
if mult == N:
    for item in mult_list:
        print(f' {item}', end='')
    print('')
else:
    print(0)
