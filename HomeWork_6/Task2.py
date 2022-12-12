# 2- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
import math

def Create_list():
    """ Creating list of random numbers

    args -> None
    returns -> list of numbers
    """
    numbers = [random.randint(1, 10) for i in range(int(input('Введите количество чисел:\n')))]
    return numbers
   
def Multiply_elem(data_list):
    """ Find multiplication of a first and last number in list

    args -> list of numbers
    returns -> list of numbers
    """
    res_list = [data_list[i]*data_list[(-1) + (-i)] for i in range(math.ceil(len(data_list)/2))]
    return res_list

elements = Create_list()
resault = Multiply_elem(elements)
print (f'{elements} => {resault}')