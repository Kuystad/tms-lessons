from functools import reduce

def my_join(string, slash):
    return reduce(lambda x,y: x + slash + y, string)
user = input('Ent a smth' ).split()
slash = input()
print(my_join(user, slash))

