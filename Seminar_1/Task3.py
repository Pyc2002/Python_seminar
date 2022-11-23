#1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#    
#    *Примеры:* 
#    
#    - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5



 



# n = abs(int(input('Введите число:\n')))

# n_reversed = n * -1

# for num in range(n_reversed, n+1):
#     print(n_reversed, end = ' ')  
#     n_reversed += 1

number=abs(int(input('Введите число:\n')))
r=range(-number,number+1)
arr=list(r)
print(arr)
