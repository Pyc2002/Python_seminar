# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol

def Rec_text():
    """ Encode a text and saving it in file
    args -> None  
    returns -> list of tuples
    """
    string = input('Введите текст: \n') + ' '
    res_str = ()
    result =''
    count = 1
    for i in range(len(string)-1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            res_str += (count, string[i])
            count = 1
    for item in res_str:
        if item != 1: result += str(item)
    with open ('HomeWork_4/Files/rec_text(Task_5).txt', 'w') as data:
        data.write(result)
    print (res_str) # для проверки
    print (result) # для проверки
    return res_str
    
    
def Decoding(text):
    """ Decode a text and saving it in file
    args -> list of tuples 
    returns -> None
    """
    result = ''
    for i in range(0, len(text)-1, 2):
        result += (text[i] * text[i+1])
    with open ('HomeWork_4/Files/decode_text(Task_5).txt', 'w') as data:
        data.write(result)
     
    print(result) # для проверки
  
        
text = Rec_text()
Decoding(text)