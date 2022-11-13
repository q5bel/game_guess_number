from random import randint

def guess_game():
    guess = 0
    count = 0
    num = randint(1, 100)
    print('Программа сгененрировала случайное число от 1 до 100, попробуйте угадать это число.')
    while guess != num:
        count += 1
        guess = int(input('Введите число: '))
        if guess == num:
            print(f'Вы угадали за {count} попыток, поздравляем!')
        elif guess > num:
            print('Слишком много, попробуйте еще раз')
        elif guess < num:
            print('Слишком мало, попробуйте еще раз')

guess_game()
