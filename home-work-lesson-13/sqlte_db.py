import sqlite3


def create_table():
    with sqlite3.connect('sqlite.db') as connection:
        connection.execute('CREATE TABLE IF NOT EXISTS user'
                           '(number VARCHAR,'
                           ' first_name VARCHAR)')


def save_contact():
    with sqlite3.connect('sqlite.db') as connection:
        first_name = input('Ent u name: ')
        number = input('Ent telephone numb: ')
        connection.execute('INSERT INTO user VALUES(?, ?)', (number, first_name))
    print('Contact saved!')


def show_contact():
    with sqlite3.connect('sqlite.db') as connection:
        result = connection.execute('SELECT * FROM user ORDER BY first_name')
    print(result.fetchall())


def update_number():
    with sqlite3.connect('sqlite.db') as connection:
        first_name = input('Enter the name of the contact whose number you want to change: ')
        number = input('Enter a new contact number: ')
        result = connection.execute('UPDATE user SET number = ? WHERE first_name = ?', (number, first_name))
    print('Contact saved!')


def main():
    while True:
        create_table()
        numbers = input(
            '0. Exit\n1. Add a new number\n2. Display the entire list of contacts in alphabetical order\n3. Update contact numbers\n')
        if numbers == '0':
            break

        if numbers == '1':
            save_contact()
        if numbers == '2':
            show_contact()
        if numbers == '3':
            update_number()


if __name__ == "__main__":
    main()
