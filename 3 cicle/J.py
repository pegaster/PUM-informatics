N = int(input())
mult = 0
mult_list = []
for i in range(1, N):
    if N % i == 0:
        mult += i
        mult_list.append(i)
if mult == N:
    for item in mult_list:
        print(f' {item}', end='')
    print('')
else:
    print(0)
