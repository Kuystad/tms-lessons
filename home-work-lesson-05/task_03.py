def generate_squares(*args: int):
    return [i ** 2 for i in args]

assert generate_squares(1, 2, 3) == [1, 4, 9]
assert generate_squares(4, 5, 6) == [16, 25, 36]

print(generate_squares(1, 2, 3))



