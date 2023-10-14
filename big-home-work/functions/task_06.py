def hello_world():
    print('Hello world')


def my_sum(a, b):
    return a + b



def simple_compare(a, b) -> int:
    return a < b



def compare(a, b):
    if a < b:
        return -1
    if a > b:
        return 1
    if a == b:
        return 0



def filter_negative_number(numbers):
    new_numbers = []
    for i in numbers:
        if i >= 0:
            new_numbers.append(i)
    return new_numbers


n = int(input("Enter task number: "))
if n == 1:
    hello_world()
elif n == 2:
    a = int(input('Enter the first numb: '))
    b = int(input('Enter the second numb: '))
    result = my_sum(a, b)
    print(f'Sum of Numbers: {result}')
elif n == 3:
    a = int(input('Enter the first numb: '))
    b = int(input('Enter the second numb: '))
    result = simple_compare(a, b)
    print(f'The first numb is less then second numb: {result}')
elif n == 4:
    a = int(input('Enter the first numb: '))
    b = int(input('Enter the second numb: '))
    result = compare(a, b)
    print(f'Result of compare: {result}')
elif n == 5:
    user_input = input('Enter the numb with a space: ')
    numbers = []
    for i in user_input.split():
        numbers.append(int(i))
    filt_numbs = filter_negative_number(numbers)
    print(f'Delete negative numb in u list: {filt_numbs}')
else:
    print('Sorry, there is no task with this numb. ')



