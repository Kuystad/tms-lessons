def remove_vowels(letters):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return list(filter(lambda x: x.lower() not in vowels, letters))


user_input = input("Enter the letters: ").split()
print(remove_vowels(user_input))
