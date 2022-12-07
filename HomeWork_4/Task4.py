# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

import string


def Rec_text(text, num):
    """ Caesar's cipher - encryption techniques
    args -> text, key

    returns -> replaced text in file
    """
    top_secret = ''
    alpha_list = [chr(i) for i in range(ord('a'), ord('z')+1)] # подсмотрено в интернете (не совсем понял как работает)
    alphabet = ''.join(alpha_list)
    for letter in text:
        letter_alphabet = alphabet.find(letter)
        new_letter = (letter_alphabet + num) % len(alphabet)
        if letter in alphabet:
            top_secret += alphabet[new_letter]
        else: top_secret += letter
            
    secret_text = open('HomeWork_4/Files/secret(Task_4).txt', 'w')
    secret_text.writelines(top_secret)
    secret_text.close



def Decoding_text(num):
    """ Caesar's cipher - decryption techniques
    args -> key

    returns -> return initial text in file
    """
    path = 'HomeWork_4/Files/secret(Task_4).txt'
    data = open(path, 'r')
    text = data.read()
    data.close()
    new_text = ''
    alpha_list = [chr(i) for i in range(ord('a'), ord('z')+1)]
    alphabet = ''.join(alpha_list)
    for letter in text:
        letter_alphabet = alphabet.find(letter)
        old_letter = (letter_alphabet - num) % len(alphabet)
        if letter in alphabet:
            new_text += alphabet[old_letter]
        else: new_text += letter
        
    secret_text = open('HomeWork_4/Files/open_secret(Task_4).txt', 'w')
    secret_text.writelines(new_text)
    secret_text.close

number = int(input('Введите количество символов для шифрования:\n'))
text_enc = input('Введите текст(пока что только на латинице):\n')
encoding = Rec_text(text_enc, number)
decoding = Decoding_text(number)