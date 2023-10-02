def date(day, month):
    if day <= 0 or month <= 0:
        return False
    else:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if day <= months[month - 1]:
            if month <= 12:
                return True
        return False


day = int(input('Day: '))
month = int(input('Month: '))
print(date(day, month))

#Смог сделать только после прохождения темы "Функция". Долго мучался, честно говоря :)









