# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# def input_list():    
#     data = input('Введите значения в списке через пробел:\n').split(" ")     
#     return data

def find_value():    
    what_find = input('Что ищем?\n')    
         
    result = [i[0] for i in enumerate(input('Введите значения в списке через пробел:\n').split(' ')) if i[1] in what_find]
    if len(result) > 1:
        print(f'Ответ: {result[1]}')
    else: print('Ответ: -1')
   


result = find_value()
# print(result)