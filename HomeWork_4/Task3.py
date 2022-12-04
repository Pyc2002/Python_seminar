# В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Энакин Скайуокер 5
# Фредди Меркури 3
# Александр Пушкин 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# ЭНАКИН СКАЙУОКЕР 5
# Фредди Меркури 3
# Александр Пушкин 4

names = open('HomeWork_4/Files/names(Task3).txt', 'w')
names.write('Ivanov Ivan Ivanovich: 5\n')
names.write('Petrov Petr Petrovich: 4\n')
names.write('Sidorov Sidor Sidorovich: 5\n')
names.write('Durakov Durak Durakovich: 2\n')
names.write('Phytonov Phyton Phytonovich: 3\n')
names.write('Gitov Git Gitovich: 3\n')
names.close()

def Create_dictionary(text):
    """Create dictionary from file and split it
    
    args -> file.txt

    returns -> dictionary
    """

    with open('HomeWork_4/Files/names(Task3).txt') as file:
        lines = file.read().splitlines() # чтобы не было пустых строк


    dict ={}
    for i in lines: 
        key,value = i.split(': ') # Разделяем каждую строку (в key будет - фио, в value - оценка)
        dict.update({key:value})
    return dict

def Shift_dict (temp_dict):
    """Create new dictionary with shift letters with If
    
    args -> dictionary

    returns -> new dictionary
    """
    res_dict = {}
    for key in temp_dict.keys():
        
        if int(temp_dict[key]) > 4: res_dict.update({key.upper():temp_dict[key]})
        else: res_dict[key] = temp_dict[key]
    return res_dict

income_dict = Create_dictionary(names)
resault_dict = Shift_dict(income_dict)

names = open('HomeWork_4/Files/names(Task3).txt', 'w')
for key, value in resault_dict.items():
    names.write('{} : {}\n'.format(key,value))
names.close