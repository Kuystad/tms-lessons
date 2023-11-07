from person import Person

my_friends = [Person('Andrey', 33, 'M'),
              Person('Anton', 22, 'M'),
              Person('Kate', 27, 'F')]

for friends in my_friends:
    friends.print_person_info()


def get_oldest_person(oldest_friends):
    oldest_friends = max(oldest_friends, key=lambda my_friends: my_friends.age)
    return oldest_friends


def filter_male_person(friends):
    male_friends = filter(lambda person: person.gender == 'M', friends)
    return list(male_friends)


print('The oldest among friends: ')
oldest_friend = get_oldest_person(my_friends)
oldest_friend.print_person_info()

print('Male friends: ')
male_friends = filter_male_person(my_friends)
for friend in male_friends:
    friend.print_person_info()
