# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# Пример:
# - quarter = 1 = x∈(0, ∞) u y∈(0,∞)

quarter = int(input('Введите номер четверти:\n'))
if quarter < 1 or quarter > 4: print ('Ошибка! Введите число от 1 до 4')
elif quarter == 1: print ('quarter = 1 = x∈(0, ∞) u y∈(0,∞)')
elif quarter == 2: print ('quarter = 2 = x∈(∞, 0) u y∈(0,∞)') 
elif quarter == 3: print ('quarter = 3 = x∈(∞, 0) u y∈(∞,0)') 
else: print ('quarter = 4 = x∈(0, ∞) u y∈(∞,0)')
