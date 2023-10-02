for i in range(101):

    while True:
        answer = input('Should we break? ')
        if answer != 'no' and answer != 'yes':
            print('Dont understand u')
        else:
            break

    if answer == 'yes':
        break
    print(i)



