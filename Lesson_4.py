#Задание 1

# def salary ():
#     hour = float(input('Укажите количество отработанных часов: '))
#     position = float(input('Укажите сумму оплаты труда за час: '))
#     premium = float(input('Укажите размер премии: '))
#     salary_1 = hour * position
#     return salary_1 +premium
#
# print(f'Размер оклада сотрудника  {salary()}')

#Задание 2

# old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# new_list = [el for el_1, el in zip(old_list, old_list[1:]) if el > el_1]
# print(new_list)

#Задание 3

# my_list_3 = range(20,240)
# new_list_3 = [el for el in my_list if el % 20 == 0 or el % 21 == 0]
# print(new_list_3)

#Задание 4
'''Попробовала с set  но он встает в порядке возростания'''

# my_list_4 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# new_list_4_1 = list(set(my_list_4))
# print(new_list_4_1)
# new_list_4_2 = [el for el in my_list_4 if my_list_4.count(el) == 1]
# print(new_list_4_2)

#Задание 5
# from functools import reduce
#
# my_list_5 = range(100, 1001)
#
# new_list_5 = [el for el in my_list_5 if el % 2 == 0]
# print(new_list_5)
# print(f'Произведение всех чисел нового списка равно {reduce(lambda x, y: x*y, new_list_5)}')

#Задание 6

# from itertools import count, cycle

# a = int(input('Введите целое число от 0 до 10: '))
#
# '''вариант 1'''
# my_list = [a for a in range(a, 11)]
# print(my_list)
#
# '''вариант 2'''
# for n in count(a):
#     print(n)
#     if n == 10:
#         break

# my_list_6_2 = [1, 1, 2, 5, 6, 8, 1, 5, 8, 9]
# for el in cycle(my_list_6_2):
#     print(list(set(my_list_6_2)))
#     if el == 1:
#         break

#Задание 7
from math import factorial

def fact (n):
    for i in range(n):
        print(f'{i}! = ')
        yield factorial(i)

a = int(input('Введите число факториал которого хотите вычислить: '))

for el in fact(a):
    print(el)
