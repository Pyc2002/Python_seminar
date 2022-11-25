# def give_int(input_string):
#     while True:
#         try:
#             num = int(input(input_string))
#             return num
#         except:
#             print('Попробуйте еще раз. Вы ввели не число')


# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81


list_random = []
number = int(input('Введите число '))

for i in range(0, number):
    list_random.append((-3)**i)
print(list_random)
