from random import randint, choice
from decouple import config

def casino():
    user_input = input('Начнем? [y]')
    if user_input == 'y':
        while True:
            balance = config('BALANCE', cast=int)
            if user_input == 'y' and balance > 0:
                slot_input = int(input('На какой слот ставим: '))
                if slot_input > 30:
                    print('Всего 30 слотов.')
                else:
                    balance_input = int(input('Сколько ставим: '))
                    if balance_input > balance:
                        print(f'На вашем балансе недостаточно средств. Ваш текущий счет равен {balance}')
                    else:
                        random_slot = randint(1, 30)
                        if slot_input == random_slot:
                            balance += balance_input*2
                            print(f'Вы выиграли! Ваш текущий счет равен {balance}')

                        else:
                            balance -= balance_input
                            print(f'Вы проиграли! Ваш текущий счет равен {balance}')
    else:
        print('ну ладноооо...')
#
#
# casino()
#
