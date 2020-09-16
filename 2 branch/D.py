position = input().split()
x = float(position[0])
y = float(position[1])

check = x < 2 and y > 0 and x-y > 0 and (x*x+y*y)-4 > 0
print('YES' if check else 'NO')
