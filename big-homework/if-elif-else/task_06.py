month = int(input())
if month == 12 or month == 1 or month == 2:
    print('Winter')
elif 3 <= month <= 5:
    print('Spring')
elif 6 <= month <= 8:
    print('Summer')
elif 9 <= month <= 11:
    print('Autumn')
else:
    print('This month if not found, try again')

