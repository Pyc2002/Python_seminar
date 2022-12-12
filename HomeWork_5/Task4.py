# 4-Создайте два списка — один с названиями языков программирования, другой — с их нумерацией.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая (обязательно используйте tuple unpacking) — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, 
# с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. 1
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

from functools import reduce

def Create_tuple(languages, numbers):
    """ Create tupleon.

    args -> None
    returns: tuple(int, str)
    """
    
    languages = list(map(str.upper, languages))
    first_tuple = list(zip(numbers, languages))
    print(first_tuple) # для проверки
    return first_tuple
    

def Main(list_tuple):
    """ Tuple unpacking, count summary using ord 
    
    args ->: list with tuples
    returns -> result list of tuple and summary (int)
    """

    numbers_list, languages_list = zip(*list_tuple)
    temp_list = ()
    for item in languages_list:
        sum = 0
        for i in item:
            sum += ord(i)
        temp_list += (sum, item)
    print (temp_list) # для проверки
    # sum = 0
    # num_list = []
    # names = []
    # count = 4
    # for i in range(2, len(temp_list)-1, 2):
    #     if temp_list[i] % (count/2) == 0:   # только это смог придумать (переменную count), чтоб не повторять работу, которую разирали на семинаре 
    #         num_list.append(temp_list[i])
    #         names.append(temp_list[i +1])
    #         sum += temp_list[i]
    #     count +=2 
    # result = list(zip(num_list, names))
    result_list = []
    result = 0
    for number, language in temp_list[::]:
        points = reduce(lambda a,b: a+b, [ord(char) for char in language])
    if points % number == 0:
        result += points
    result_list.append((points, language))

    return result, sum

 
languages = ['python', 'rust', 'c#', 'c++', 'kotlin', 'js', 'java', 'swift', 'php']
numbers  = [i for i in range(1, len(languages)+1)]

first_tuple = Create_tuple(languages, numbers)
res_tuple, res_sum = Main(first_tuple)
print (f'{res_tuple}\n Сумма чисел: {res_sum}')