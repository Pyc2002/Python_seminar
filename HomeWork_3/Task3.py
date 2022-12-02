# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

import random

def Create_list():
    """Create list with float  numbers

    args -> none

    returns -> list
    """
    count = int(input('Введите количество чисел:\n'))     
    numbers = []
    for i in range(count):
        numbers.append(round(random.uniform(1,10),3))
    return numbers

def Find_MinMax(list_numbers):
    """ Find difference between max and min of fractional parts of numbers

    args -> list of float numbers

    returns -> difference 
    
    """
    max = 0.0
    min = 1.0
    for num in range(len(list_numbers)):
        fractional = list_numbers[num] % 1 # для извлечения дробной части 
        if fractional > max: max = fractional
        if fractional < min: min = fractional
    print (max,min)
    diff = round((max - min),3)
    return diff


elements = Create_list()
print(elements)
resault = Find_MinMax(elements)
print (f'Ответ: {resault} или {int(resault * 1000)}')