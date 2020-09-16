position = input().split()
x = float(position[0])
y = float(position[1])

check = y < (2 - x ** 2) and ((y > 0) or (x < y < 0))
print('YES' if check else 'NO')