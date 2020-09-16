a = int(input())
b = int(input())
c = int(input())

check = (a < (b + c)) and (b < (a + c)) and (c < (a + b))
print('YES' if check else 'NO')