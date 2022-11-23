#2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#    Примеры:
#    - 1, 4, 8, 7, 5 -> 8
#   - 78, 55, 36, 90, 2 -> 90

print('Введите первое число')
first_num = int(input())
print('Введите второе число')
second_num = int(input())
print('Введите третье число')
third_num = int(input())
print('Введите четвертое число')
fourth_num = int(input())
print('Введите пятое число')
fifth_num = int(input())
max_num = first_num
if second_num > max_num : max_num = second_num
elif third_num > max_num : max_num = third_num
elif fourth_num > max_num : max_num = fourth_num
else: max_num = fifth_num
print (f'{fifth_num}, {second_num}, {third_num}, {fourth_num}, {fifth_num} -> {max_num}')

# ошибка