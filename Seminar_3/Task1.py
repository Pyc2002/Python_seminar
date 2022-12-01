# 1.	Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число. 
# ['gfh5', 'gfh2', '67', 'jy32', '3put'] - ищем 32 - находим по индексу 3 
# list_1 = ['gfh5', 'gfh2', '67', 'jy32', '3put']
# n = 6


def input_list():    
    data = input('Введите значения в списке через пробел:\n').split(" ")     
    return data

def find_value(data_list):     
    what_find = input('Кого ищем то?\n')     
    resault = []   
    for i in range(len(data_list)):         
        if what_find in data_list[i]:             
            resault.append(i)
    return resault

elements = input_list()
resault_list = find_value(elements)
print (f'число присутствует в списке по индексам: {resault_list}')
