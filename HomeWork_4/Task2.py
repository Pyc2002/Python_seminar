# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. 
# Не использовать множества.
# Постарайтесь решить за одно условие
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

import random

def Create_list():
    """ Create sorted list with random numbers

    args -> none

    returns -> list    
    """
    count = int(input('Введите количество чисел:\n'))     
    numbers = []
    for i in range(count):
        numbers.append(random.randint(1,5))
    numbers.sort()

    return numbers

def Del_similar_num(num_list):
    """ Remove same numbers in list

    args -> list

    retuns -> list
    """
    res = []
    for i in num_list:
        if i not in res: res.append(i)
    return res

numbers = Create_list()
resault = Del_similar_num(numbers)
print (f'{numbers} -> {resault}')