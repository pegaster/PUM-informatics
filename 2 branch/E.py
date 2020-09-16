import math
position = input().split()
x = float(position[0])
y = float(position[1])

check = y < math.sin(x) and 0 < y < 0.5 and math.pi > x > 0
print('YES' if check else 'NO')