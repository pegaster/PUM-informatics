N = int(input())
mult = 3
mult_list = [1, 2]
end = N // 2
i = 3
if N % 2 == 0:
    while i < end:
        if N % i == 0:
            end = N // i
            mult += i
            if end != i:
                mult += end
            mult_list.append(i)
        i += 1
    mult += N // 2
    for item in mult_list:
        if N > N // item > item:
            mult_list.append(N // item)
    mult_list.sort()
    if mult == N:
        for item in mult_list:
            print(f' {item}', end='')
        print('')
if mult != N or N == 3:
    print(0)
