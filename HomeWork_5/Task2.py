# 2- Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

def Who_is_first():
    """ random choice who will move first
    args -> None
    returns -> first    
    """

    first = random.randint(0,2)
    if first: print('Первым ходит игрок 1')
    else: print('Первым ходит игрок 2')
    return first

def Input_sweets(num):
    """ make a move and testing it

    args -> mark (int, inputs by player)
    returns -> movment or message with mistake
    """
    sweets = int(input(f'Введите количество конфет, не более {num} шт.:\n'))
    while sweets < 1 or sweets > num:
        sweets = int(input(f'ОШИБКА! Количество конфет должно быть от 1 до {num} шт.:\n'))
    return sweets

def The_game(max_sweet, num):
    """ main algorithm, a lot of prints
    args -> int, int
    returns -> prints
    """
    first = Who_is_first()
    gamer_1 = 0
    gamer_2 = 0
    while max_sweet > 0:
        sweets = Input_sweets(num)
        if first:
            gamer_1 += sweets
            max_sweet -= sweets
            first = 0
            if max_sweet <= 0: 
                print('Победил игрок 1, все конфеты достаются ему!')
                break
            else:
                print(f'У игрока 1 всего: {gamer_1} конфет')
                print(f'На столе осталось {max_sweet} конфет')
                print('        ')
                print('Игрок 2, Ваша очередь!')
        else:
            gamer_2 += sweets
            max_sweet -= sweets
            first = 1
            if max_sweet <= 0: 
                print('Победил игрок 2, все конфеты достаются ему!')
                break
            else:
                print(f'У игрока 2 всего: {gamer_2} конфет')
                print(f'На столе осталось {max_sweet} конфет')
                print('        ')
                print('Игрок 1, Ваша очередь!')


def Bot_level(level, max_sweet, num): 
    """ Bots movement
    args -> string (level), int, int
    returns -> int
    """
    if level == '1': sweets = max_sweet % (num + 1)
    else: sweets = random.randint(1,num)
    return sweets


def The_game_bot(max_sweet, num, level):
    
    first = random.randint(0,2)
    gamer_1 = 0
    bot = 0
    if first: print('Первым ходит игрок')
    else: print('Первым ходит компьютер')
    while max_sweet > 0:
        if first:
            sweets = Input_sweets(num)
            gamer_1 += sweets
            max_sweet -= sweets
            first = 0
            if max_sweet <= 0: 
                print('Победил игрок, все конфеты достаются ему!')
                break
            else:
                print(f'У игрока всего: {gamer_1} конфет')
                print(f'На столе осталось {max_sweet} конфет')
                print('        ')
        else:
            sweets = Bot_level(level, max_sweet, num)
            bot += sweets
            max_sweet -= sweets
            first = 1
            if max_sweet <= 0: 
                print('Победил компьютер, все конфеты достаются ему!')
                break
            else:
                print (f'Компьютер взял {sweets} конфет')
                print(f'У компьютера всего: {bot} конфет')
                print(f'На столе осталось {max_sweet} конфет')
                print('        ')
                print('Игрок, Ваша очередь!')

number_of_sweets = abs(int(input('Введите общее количество конфет:\n')))
sweets_per_round = abs(int(input('Введите максимальное количество конфет, которое можно забрать за 1 ход:\n')))
who_plays = input('Выберете с кем будете играть:\n С человеком - нажмите 1\n С компьютером - нажмите 2\n')
if who_plays == '1': The_game(number_of_sweets, sweets_per_round)
else: 
    level = input('Выберете уровень:\n Сильный бот - нажмите 1\n Слабый бот - нажмите 2\n')    
    The_game_bot(number_of_sweets, sweets_per_round, level)
