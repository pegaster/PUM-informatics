position = input().split()
x = float(position[0])
y = float(position[1])
check = ((x ** 2 + y ** 2) < 1) and ((x < 0 and y < 0) or (x < 0 and y > 0) or (x > 0 and y > x)) 
print('YES' if check else 'NO')