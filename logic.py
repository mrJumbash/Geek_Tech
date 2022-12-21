from random import randint, choice
from decouple import config

def casino():
    user_input = input('Начнем? [y]')
    balance = config('MY_MONEY', cast=int)
    my_money = config('MY_MONEY', cast=int)
    if user_input == 'y':
        while True:
            if user_input == 'y' and balance > 0:
                slot_input = int(input('На какой слот ставим: '))
                if slot_input > 30:
                    print('Всего 30 слотов.')
                else:
                    balance_input = int(input('Сколько ставим: '))
                    if balance_input > balance:
                        print(f'На вашем балансе недостаточно средств. Ваш текущий счет равен {balance}')
                        balance_input2 = input('Желаете продолжить? [y], [n]')
                        if balance_input2 == 'n':
                            print(f'Ваш баланс {balance}! До скорой встречи.')
                            break
                    else:
                        random_slot = randint(1, 30)
                        if slot_input == random_slot:
                            balance += balance_input*2
                            print(f'Вы выиграли! Ваш текущий счет равен {balance}')
                            win_input = input('Желаете продолжить? [y], [n]')
                            if win_input == 'n':
                                print(f'Ваш баланс {balance}! До скорой встречи.')
                                break
                        else:
                            balance -= balance_input
                            print(f'Вы проиграли! Ваш текущий счет равен {balance}')
                            lose_input = input('Желаете продолжить? [y], [n]')
                            if lose_input == 'n':
                                print(f'Ваш баланс {balance}! До скорой встречи.')
                                break
        if balance > my_money:
            print('Вы в выигрыше!')
        else:
            print('Вы в проигрыше!')
    else:
        print('ну ладноооо...')
