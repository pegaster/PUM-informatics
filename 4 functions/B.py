num = input()
reverse_num = ''
for i in range(len(num) - 1, -1, -1):
    reverse_num += num[i]
print(reverse_num)
