from datetime import date


class Person:

    def __init__(self, full_name: str, age: int, gender: str):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    def print_person_info(self):
        print(f'Person: {self.full_name} {self.gender}, {self.age} years old')

    def get_birth_years(self):
        return int(str(date.today())[0:4]) - self.age

#person = Person('Ivan Ivanov', 20, 'M')
#person.print_person_info()
#print(person.get_birth_years())