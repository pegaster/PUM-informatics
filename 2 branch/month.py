month_number = int(input())
result = 0
if ((0 < month_number <= 7) and month_number % 2 == 0) or ((7 < month_number <= 12) and (month_number % 2 != 0)):
    result = 30

elif ((0 < month_number <= 7) and month_number % 2 != 0) or ((7 < month_number <= 12) and (month_number % 2 == 0)):
    result = 31

if month_number == 2:
    result = 28
print(result)