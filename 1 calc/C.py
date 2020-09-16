pos1 = input().split(' ')
pos2 = input().split(' ')
space = (abs(float(pos1[0]) - float(pos2[0])) ** 2 + abs(float(pos1[1]) - float(pos2[1])) ** 2) ** 0.5
print('{:.3f}'.format(space))
