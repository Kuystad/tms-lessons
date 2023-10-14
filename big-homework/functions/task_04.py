def compare(a, b):
    if a < b:
        return -1
    if a > b:
        return 1
    if a == b:
        return 0

print(compare(1, 2))
print(compare(3, 2))
print(compare(1, 1))