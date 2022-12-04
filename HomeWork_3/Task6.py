#  Бухгалтер Люба заполняет ведомость по зарплате. У Любы есть два файла - один с фио, другой - с зарплатой за декабрь.

# Ей нужно создать третий файл вида "фио, зарплата".
# Но Люба совершила ошибку. Она забыла, что в декабре все работники должны получить зарплату по повышенному коэффициенту: 1.5
# А еще у босса есть список любимчиков, которым повышенный коэффициэнт будет 2, их фио нужно выделить высоким регистром: они получат зарплату раньше.
# Создайте сначала словарь на основе первых двух файлов, а дальнейшие действия - с созданным словарем.

# Пример:
# Файл 1: (разумеется, у вас больше)
# Гарри Джеймс Поттер
# Дадли Вернон Дурсль

# Файл 2:
# 10000
# 12000

# Финальный файл:
# Гарри Джеймс Поттер, 15000
# ДАДЛИ ВЕРНОН ДУРСЛЬ 24000


names = open('Files/names(HW3_Task6).txt', 'w')
names.write('Ivanov Ivan Ivanovich\n')
names.write('Petrov Petr Petrovich\n')
names.write('Sidorov Sidor Sidorovich\n')
names.write('Durakov Durak Durakovich\n')
names.write('Phytonov Phyton Phytonovich\n')
names.write('Gitov Git Gitovich\n')
names.close()


salary = open('Files/salary(HW3_Task6).txt', 'w')
salary.write('50000\n')
salary.write('70000\n')
salary.write('80000\n')
salary.write('100000\n')
salary.write('70000\n')
salary.write('80000\n')
salary.close()


def Create_dictionary(text1, text2):
    """Create dictionary from two files
    
    args -> file.txt, text.txt

    returns -> dictionary
    """

    with open('Files/names(HW3_Task6).txt') as file: #Читаем файл
        lines1 = file.read().splitlines() # read().splitlines() - чтобы небыло пустых строк
    with open('Files/salary(HW3_Task6).txt') as file: 
        lines2 = file.read().splitlines()
    
    
    dict ={}
    # for key in lines1:
    #     for value in lines2:
    #         dict.update({key:int(value)})

    for i in range(0,len(lines1)):
        dict[lines1[i]] = lines2[i]
        dict.update({lines1[i]: int(lines2[i])})
    return dict

def Change_dictionary(temp_dict, names):
    """ Create new dictionary using dictionary and names of people who 
    will get higher salary

    args -> dictionary, names

    returns -> dictionary    
    """
    res_dict = {}
    for key, value in temp_dict.items():
        if key in names:
            res_dict.update({key.upper():int(temp_dict[key])*2})
        else: res_dict[key] = int(temp_dict[key]*1.5)
    return (res_dict)

monthly_salary = Create_dictionary(names, salary)
lucky_man = 'Petrov Petr Petrovich', 'Durakov Durak Durakovich'
december_sal = Change_dictionary(monthly_salary, lucky_man)


december_salary = open('Files/december_salary(HW3_Task6).txt', 'w')
for key, value in december_sal.items():
    december_salary.write('{} : {}\n'.format(key,value))
december_salary.close()
    





