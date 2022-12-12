# 5 - Есть список случайных чисел в промежутке от 1 до 100, количеством 200. Создайте список кортежей, первый элемент которого - индекс элемента, 
# а второй - сам элемент, при условии, что они не совпадают.
# [1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

import random


def  Multiple_of_five(list):  # Создал только, чтобы применить функцию filter, можно было бы и без этой функции
    """ Find sum of elements of tuple witch multiples of five

    args -> tuple
    returns -> list
    """
    result = [i for i in range(len(list)-1) if not (list[i]+list[i+1]) % 5]
    return result

list_tuple = [i for i in enumerate([random.randint(1, 100) for i in range(1,200)]) if i[0] != i[1]]
res_tuple = list(filter(Multiple_of_five, list_tuple))

print(list_tuple)
print(' ')
print (res_tuple)