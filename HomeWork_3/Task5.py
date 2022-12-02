# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


def Fibonacci(num):
    """ Fibonacci number and NegaFibonacci

    args -> number

    returns ->  list  
    """
    res = [0,1]
    nega_res = [0,1]
    for i in range(1, num):
        res.append(res[-1] + res[-2])      
        nega_res.append(nega_res[-2] - nega_res[-1])
    nega_res.reverse()
    
    res_list = nega_res[:-1] + res[:]
    return res_list

number = abs(int(input('Введите число:\n')))
resault = Fibonacci(number)
print(resault)
