import random


def get_random_digits(count: int) -> str:
    result = ''
    for i in range(count):
        result += str(random.randint(1, 9))
    return result


class BankAccount:
    def __init__(self, card_holder):
        self.card_holder = card_holder.upper()
        self.money = 0
        self.account_number = get_random_digits(20)
        self.card_number = get_random_digits(16)


class Bank:
    def __init__(self):
        self.__bank_accounts: list[BankAccount] = []

    def open_account(self, card_holder: str):
        account = BankAccount(card_holder)
        self.__bank_accounts.append(account)
        return account

    def __get_account(self, account_number) -> BankAccount:
        for bank_account_in_lst in self.__bank_accounts:
            if bank_account_in_lst.account_number == account_number:
                return bank_account_in_lst

    def get_all_bank_account(self):
        return self.__bank_accounts

    def add_money(self, account_number, money):
        account = self.__get_account(account_number)
        account.money += money

    def transfer_money(self, from_account_number, to_account_number, money):
        account_01 = self.__get_account(from_account_number)
        account_02 = self.__get_account(to_account_number)
        account_01.money -= money
        account_02.money += money

    def external_transfer(self, from_account_number, to_external_number, money):
        external_account = self.__get_account(to_external_number)
        account = self.__get_account(from_account_number)
        external_account.money += money
        account.money -= money
        print(f'Банк перевёл {money}$ с вашего счёта '
              f'{from_account_number} на внешний счёт '
              f'{to_external_number}')


class Controller:
    def __init__(self):
        self.bank = Bank()

    def run(self):
        print('Здравствуйте, наш банк открылся!')

        while True:
            print('Выберите действие: ')
            print('0. Завершить программу')
            print('1. Открыть новый счёт')
            print('2. Просмотреть открытые счета')
            print('3. Положить деньги на счёт')
            print('4. Перевести деньги между счетами')
            print('5. Совершить платёж')

            result = int(input())
            if result == 0:
                print('До свидания!')
                break


            elif result == 1:
                card_holder = input('Введите Ваше Имя и Фамилию: ')
                account = self.bank.open_account(card_holder)
                print(f'Счёт {account.account_number} создан!')

            elif result == 2:
                print('Все счета:')
                for account in self.bank.get_all_bank_account():
                    print(f'Cчёт: {account.account_number}')
                    print(f'   Остаток на счету: {account.money}$')
                    print(f'   Номер карты: {account.card_number}')
                    print(f'   Держатель карты: {account.card_holder}')

            elif result == 3:
                account_number = input(('Введите номер счета: '))
                money = float(input('Введите сумму: '))
                self.bank.add_money(account_number, money)

            elif result == 4:
                from_account_number = input(('Введите номер счета отправителя: '))
                to_account_number = input(('Введите номер счета получателя: '))
                money = float(input('Введите сумму: '))
                self.bank.transfer_money(from_account_number, to_account_number, money)

            elif result == 5:
                extarnel_number = input(('Введите номер внешнего счета: '))
                from_account_number = input(('Введите номер счета отправителя: '))
                money = float(input('Введите сумму: '))
                self.bank.external_transfer(extarnel_number, from_account_number, money)
            else:
                print('Вы ввели не поддерживаемую команду! ')


if __name__ == '__main__':
    controller = Controller()
    controller.run()
