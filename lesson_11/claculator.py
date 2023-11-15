class CalculationExitException(Exception):
    pass


def input_int_number() -> int:
    while True:
        try:
            return int(input('Enter a int numbers: '))

        except ValueError as e:
            print('Error', e)
            print('Data is not correct', e)


def calculate(left: int, right: int, operation: str):
    if operation == '+':
        return left + right

    elif operation == '-':
        return left - right

    elif operation == '*':
        return left * right

    elif operation == '/':
        return left / right

    elif operation == '!':
        raise CalculationExitException

    else:
        raise ValueError(f'Unsupported operation: {operation}')


def main():
    while True:
        try:
            left = input_int_number()
            right = input_int_number()
            operation = input('Enter the operation (enter "!" to exit the program: ')
            print(calculate(left, right, operation))

        except (ValueError, ZeroDivisionError) as e:
            print('Unsupported operation', e, end='\n\n')

        except CalculationExitException as e:
            print('Finishing the program')


if __name__ == '__main__':
    main()
