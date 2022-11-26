# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# # Пример:

# # 67.82 -> 23
# # (-0.56) -> 11


number = input('Введите вещественное число:\n')
array = list(number)
array.remove('.')
if ('-' in array): array.remove('-')
print(array)
array = [int(elem) for elem in array]
sum = 0
for i in range(len(array)): sum += array[i]
print (f'{number} -> {sum}')

