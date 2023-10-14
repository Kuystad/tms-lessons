def filter_negative_number(numbers):
    new_numbers = []
    for i in numbers:
        if i >= 0:
            new_numbers.append(i)
    return new_numbers
print(filter_negative_number([1, -2, -3, 4, 5]))
print(filter_negative_number([-3, -2, -1, 0, 1, 2, 3]))

