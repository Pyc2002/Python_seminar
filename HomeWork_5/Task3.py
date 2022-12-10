# 3- Создайте программу для игры в ""Крестики-нолики"". Для определения победы вам может пригодиться функция filter. 
# Проверяйте победу после каждого хода, фильтруя столбцы, строки и диагонали по знаку хода
import random

turns = [0,1,2,3,4,5,6,7,8]
 

def game_field():
    """ Game field
    args -> None
    return -> print in console
    """
   
    print(turns[0], end = "   ")
    print(turns[1], end = "   ")
    print(turns[2])
    print('  ')
    print(turns[3], end = "   ")
    print(turns[4], end = "   ")
    print(turns[5])
    print('  ')
    print(turns[6], end = "   ")
    print(turns[7], end = "   ")
    print(turns[8]) 
   
 

def Game_step(mark,symbol):
    """ Algorithm for moving and checking winner

    args -> mark (int, inputs by player) and symbol (assigned to player)
    returns -> changed element in field, exit, if player win
    """
    while turns[mark] in ('X', 'O'):
        mark = int(input(f'ОШИБКА! Ячейка уже занята! Повторите:\n'))
    turns[mark] = symbol
    
    win_codes = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for i in win_codes:
        if turns[i[0]] == "X" and turns[i[1]] == "X" and turns[i[2]] == "X":
            return exit(print('Победил игрок 1!!!'))
        if turns[i[0]] == "O" and turns[i[1]] == "O" and turns[i[2]] == "O":
            return exit(print('Победил игрок 2!!!'))
             
   

def Test_mark():      
    """ make a move and testing it

    args -> mark (int, inputs by player)
    returns -> movment or  message with mistake
    """
    mark = int(input("Выберете ячейку: "))
    while mark < 0 or mark > 8:
        mark = int(input(f'ОШИБКА! Выберете ячеку под номерами от 0 до 8! Повторите:\n'))
    while turns[mark] in ('X', 'O'):
        mark = int(input(f'ОШИБКА! Ячейка уже занята! Повторите:\n'))
    return mark
    

    
        
def The_game():
    """ main algorithm
    
    """
    count = 0
    first = random.randint(0,2)
    if first: print('Первым ходит игрок 1')
    else: print('Первым ходит игрок 2')
    
    while count < 10:
        game_field()
        
        if first:
            symbol = "X"
            mark = Test_mark()
            Game_step(mark,symbol)
            print ('  ')
            print ('Игрок 2, Ваш ход!')
            first = 0
            count += 1
            
        else:
            symbol = "O"
            mark = Test_mark()
            Game_step(mark,symbol)
            print ('  ')
            print ('Игрок 1, Ваш ход!')
            first = 1
            count += 1
            

The_game()