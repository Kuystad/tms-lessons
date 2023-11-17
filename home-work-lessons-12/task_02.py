import re


def is_date(date: str) -> bool:
    if re.fullmatch(r'\d{2}-\d{2}-\d{4}', date):
        return True

    else:
        return False


assert is_date('03-09-2001')
assert is_date('06-07-1996')
assert not is_date('1-2-3')
