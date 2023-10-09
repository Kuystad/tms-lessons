def map_to_tuples(letters):
   return list(map(lambda x: (x.upper(), x.lower()), letters))



user = input('Enter a letters ')
l = user.split()
print(map_to_tuples(l))












