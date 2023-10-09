def remove_vowels(letters):
    vowels = ['a', 'A' , 'E', 'e','I' 'i', 'O', 'o', 'U', 'u']
    return list(filter(lambda x: x not in vowels, letters))


user_input = input("Enter the letters: ").split()
print(remove_vowels(user_input))