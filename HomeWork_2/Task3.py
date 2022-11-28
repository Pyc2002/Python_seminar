# Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]
import random

num = int(input('Введите размер массива: \n'))
array = []
for i in range(num):
    array.append(random.randint(-100,100))
    if array[i] < 0: array.insert(i+1, 0)
if array[-1] < 0: array.append(0)
print (array)
