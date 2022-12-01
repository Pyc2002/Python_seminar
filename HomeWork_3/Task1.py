# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def Create_list():
    count = int(input('Введите количество чисел:\n'))     
    numbers = []
    for i in range(count):
        numbers.append(random.randint(1,10))
    return numbers

def Find_odd (data_list):
    res = 0
    for index_number in range(len(data_list)):
        if index_number % 2 != 0: res += data_list[index_number] # Проверяем на нечетность и если True - складываем значения элементов
    return res

res_list = Create_list()
resault = Find_odd(res_list)
print (f'{res_list} -> {resault}')