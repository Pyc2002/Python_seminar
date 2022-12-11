# Задана натуральная степень n. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k.
# Пример:
# - n=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 (коэф: []) или 10*x² = 0
# Уточнения:
# n - это степень икса первого элемента полинома
# при n =3 => 5*x**3 + 18*x**2 + 7*x + 19 = 0 - коэффициенты = [5,18,7,19]
# при n=2 => 2*x² + 4*x + 5 = 0(коэф: [2,4,5]) или x² + 5 = 0 (коэф: [1,0,5]) или 10*x²(коэф: [10,0,0]) = 0
# при n=10 => 56 * x*10 = 0
# коэффициенты - это числа перед элементами полинома.
# коэффициенты могут быть нулем, кроме первого

import random

def give_int(input_string:str):
    while True:
        try:
            num = int(input(input_string))
            if num < 0:
                num = abs(num)
            return num
        except:
            print('Попробуйте еще раз. Вы ввели не число')
            
def random_list (length_list, down_border, up_border):
    '''
    Задаем список случайных целых чисел в диапазоне между down_border и up_border
    длиной length_list
    '''
    rand_list=[]
    for i in range(0,length_list):
        rand_list.append(random.randint(down_border,up_border))
    return rand_list

n = give_int('Введите число (показатель степени): \n')

coef_list = random_list (n+1, 0, 100)
if coef_list[0] == 0:
    coef_list[0] = random.randint(1, 100)

degree_list = [i for i in range(n,-1,-1)]   
print(degree_list)
print(coef_list)

result = ''
for coef, degree in zip(coef_list, degree_list):
    if coef:
        coef = coef if coef > 1 else ''
        result += (f'{coef}')
        if degree > 1:
            result += (f'x**{degree} + ')
        if degree == 1:
            result += (f'x + ')   
if result.endswith('+ '):
    result = result[:-2]   
      
result += ' = 0'

print(result)