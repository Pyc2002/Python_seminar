# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

def Find_prime_factors(num):
    """Find prime factors in number

    args -> number

    returns -> prime factors
    
    """
    fact = []
    temp = 2
    while num > 1:
        if num % temp == 0:
            fact.append(temp)
            num//= temp
        else:
            temp += 1
    res = []
    for i in fact:
        if i not in res: res.append(i)
    return res


number = abs(int(input('Введите число:\n')))
resault = Find_prime_factors(number)
print (f'{number} -> {resault}')