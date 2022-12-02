# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

#  Вариант через список:

# def Transform_in_binary(num):
#   res = []
#   while num > 0:
#     res.append( num % 2)
#     num //= 2
#   res.reverse()
#   return res

# number = abs(int(input('Введите число:\n')))
# resault = Transform_in_binary(number)
# print(resault)

#  Вариант с рекурсией: 

def Transform_in_binary(num):
    """Tranform number to the binary numeral system

    args -> number

    returns -> binary 
    
    """
    if num > 1:
        Transform_in_binary(num//2)
    print(num %2 , end = '') # "end ="  для вывода всех строчек в результате в одну

number = abs(int(input('Введите число:\n')))
print (f'{number} -> ', end ='')
Transform_in_binary(number)
