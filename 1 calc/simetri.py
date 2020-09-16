number = int(input())
thousands = number // 1000
hundreds = number // 100 % 10
dozens = number // 10 - thousands * 100 - hundreds * 10
units = number % 10

print(abs(units - thousands) + abs(dozens - hundreds) + 1)
