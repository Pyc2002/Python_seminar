#1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
#   *Примеры:* 
#   - 5, 25 -> да
#  - 4, 16 -> да
#   - 25, 5 -> да
#  - 8,9 -> нет

first_num = int(input('Введите первое число: \n'))
second_num = int(input('Введите второе число \n'))
if first_num == second_num * second_num or second_num == first_num * first_num:
    print (f'{first_num}, {second_num} -> да')
else:
    print (f'{first_num}, {second_num} -> нет')
