position = input().split()
x = float(position[0])
y = float(position[1])
check = (x > 0 and y < 1) and ((x - 1 < y > 0) or (y < 0 and ((x ** 2 + y ** 2) < 1)))
print('YES' if check else 'NO')