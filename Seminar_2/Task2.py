# 2. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

list_1 = input('Введите строку:\n')
list_2 = input('Введите строку:\n')
count = 0
for first in range(len(list_1) - len(list_2) + 1):
    if list_1[first:first+len(list_2)] == list_2:
        count += 1
print(count)

# второой вариант посимвольный:
# a = list(input())
# b = list(input())
# cnt = 0
# for i in range(len(a)-len(b)+1):
#     if a[i] == b[0]:
#         switch=True
#         for j in range(len(b)):
#             if a[i+j] != b[j]:
#                 switch=False
#                 break
#         if switch:
#             cnt += 1
# print(cnt)


# срезы:
# word = 'python'
# print(word[2:])
# print(word[:2])
# print(word[1:3])


