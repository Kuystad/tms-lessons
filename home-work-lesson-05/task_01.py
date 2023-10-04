def is_year_leap(y: int) -> bool:
    if y % 4 == 0 or y % 400 == 0:
        return True
    else:
        return False
print(is_year_leap(2001))

