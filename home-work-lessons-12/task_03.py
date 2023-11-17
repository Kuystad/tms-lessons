import re


def is_float_number(number: str) -> bool:
    if re.fullmatch(r'\d\.+\d+', number):
        return True

    else:
        False


assert is_float_number('1.1')
assert is_float_number('7.3')
assert not is_float_number('12')
