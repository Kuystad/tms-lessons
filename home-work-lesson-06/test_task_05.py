def my_decorator(func):
    def my_func_01(numb):
        print(f'The function received an input {numb}')
        result = func(numb)
        print(f'Result the function {result}')
        return result
    return my_func_01
@my_decorator
def my_func(x):
    return x ** 2

y = my_func(3)
print(f'y = {y}')


