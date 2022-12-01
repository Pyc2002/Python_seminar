# По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого.
# При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты.
# Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга.
# Процесс продолжается с места остановки аналогичным образом до последнего человека в круге. Составьте алгоритм, который проводит эту игру.
# Если хотите делать паузы, то импортируйте библиотеку time и используйте оттуда функцию sleep.
# Определите номер этого человека и количество монет, которые оказались у него в конце игры.
import random

number_players = int(input('Введите количество игроков:\n'))
list_players = list(range(1, number_players+1))
coins = [0]*number_players
players_left =[]
sum = 0
while number_players > 1:
    left_num = int(input('Введите какой участник покинет игру:\n'))
    if left_num > number_players: left_num = left_num % number_players
 
    for player in range(0, len(list_players)):
        if player < left_num: coins[player] += 1
        elif player == left_num: coins[(player + 1) %len(list_players)] += coins[player]
        else: coins[player] += 2
        sum += coins[player]
        
    
    list_players = list_players[left_num:] + list_players[:left_num-1]
    coins = coins [left_num:] + coins[:left_num-1]
    print (coins)
    print (list_players)
    number_players -= 1
    print (sum)
    
print (f'останется {list_players}-ый игорк с {sum} монетами')



