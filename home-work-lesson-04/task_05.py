n = int(input('Enter a number '))
a = 0
while n != 0:
    a += n % 10
    n //= 10
print(a)
