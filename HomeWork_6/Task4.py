# 4 - Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.



def Find_domain_name(list):
    """ Find domain_name in URL by '.'
    ''.join(url_list).split('/') -  transforms list in strig splitted by '/'

    args -> list of URL
    returns -> list of domain name
    """
    res_list = [i for i in ''.join(url_list).split('/') if '.' in i]   # Просматривая URL сайтов, заметил, что '.' есть только в доменном имени. Надеюсь, что это так )
    return res_list

url_list = ['https://github.com/Pyc2002/Python_seminar', 'https://gb.ru/lessons/281597/homework', 'https://english-fun.org/ru/content/movies/table']
print (Find_domain_name(url_list))