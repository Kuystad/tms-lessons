my_dict = {'a': 1, 'b': 6, 'c': 5}
print(max(my_dict.values()))

my_dict = {'a': 14, 'b': 6, 'c': 5}

max_value = None
for key, value in my_dict.items():
    if max_value is None or value > max_value:
        max_value = value
print(max_value)
