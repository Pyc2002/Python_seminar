# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random
import math

def Create_list():
    count = int(input('Введите количество чисел:\n'))     
    numbers = []
    for i in range(count):
        numbers.append(random.randint(1,10))
    return numbers
   

def Multiply_elem(data_list):
    res_list =[]
    for i in range(math.ceil(len(data_list)/2)): # округление в большую сторону для нечетного количества чисел
        res = data_list[i]*data_list[(-1) + (-i)] # умножаем значения первого и последнего элемента (к последнему элементу каждый раз прибавляем -1)
        res_list.append(res)
    return res_list

elements = Create_list()
resault = Multiply_elem(elements)
print (f'{elements} => {resault}')

# Вариант 2, без использования math.ceil:

# def Create_list():
#     count = int(input('Введите количество чисел:\n'))     
#     numbers = []
#     for i in range(count):
#         numbers.append(random.randint(1,10))
#     return numbers
   

# def Multiply_elem(data_list):
#     res_list =[]
#     if len(data_list) % 2 == 0:  # Проверка на четность списка, если True, то список делим пополам 
#         for i in range(len(data_list)//2):
#             res = data_list[i]*data_list[(-1) + (-i)] # умножаем значения первого и последнего элемента (к последнему элементу каждый раз прибавляем -1)
#             res_list.append(res)
#     else: 
#         for i in range(len(data_list)//2+1): # если False, то список делим пополам и прибавляем 1, чтобы увеличить размер списка 
#             res = data_list[i]*data_list[(-1) + (-i)]
#             res_list.append(res)
#     return res_list

# elements = Create_list()
# resault = Multiply_elem(elements)
# print (f'{elements} => {resault}')