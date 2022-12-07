# 1-Напишите программу, удаляющую из текста все слова, содержащие заданную строку.

# Пример:
# Пугать ты галок пугай => заданная строка "пугай" => Пугать ты галок

def Delete_symbols(text, find_text):
    """ Find and remove words in line

    args -> text, text for deleting

    returns -> result text    
    """
    text = text.split(' ')
    print (text)
    res = []
    for i in text:
        if i != find_text: res.append(i)
    res =' '.join(res)
    return res

text_str = input('Введите текст:\n')
part_text = input('Введите текст:\n')
resault = Delete_symbols(text_str, part_text)
print(resault)