# If zero not in list:
my_list = [4, 1, 2]
zero = False
for i in my_list:
    if i == 0:
        zero = True
        break

if zero:
    print('Yes')
else:
    print('No')

# If zero in list:
my_list = [0, 1, 2]
zero = False
for i in my_list:
    if i == 0:
        zero = True
        break

if zero:
    print('Yes')
else:
    print('No')
