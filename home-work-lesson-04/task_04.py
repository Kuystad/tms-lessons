import random
n = random.randint(0, 10)
while True:
    a = int(input("Enter a numb "))
    if a == n:
        print('Congrats!')
        break
    elif n > a:
        print('Dont guess right, the number is greater than the guessed number')
    else:
        print("Dont guess right, the number is less than the guessed number")



