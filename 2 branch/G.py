position = input().split()
x = float(position[0])
y = float(position[1])

check = (y > (x ** 2 - 2)) and ((y < 0) or ((y < x) or (y < -x)))
print('YES' if check else 'NO')