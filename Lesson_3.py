# Задание 1
# def delen ():
#     chisl = int(input('Введите числитель (то, что делить) функции: '))
#     znam = int(input('Введите знаменатель (то, на что делить) функции: '))
#     if znam != 0:
#         return chisl / znam
#     else:
#         print('Деление на 0 невозможно!')
#         chisl = int(input('Введите числитель (то, что делить) функции: '))
#         znam = int(input('Введите знаменатель (то, на что делить) функции: '))
#     return chisl / znam
#
# print(delen())

# Задание 2

# def info (*args):
#     name = input('Назовите ваше имя: ')
#     first_name = input('Назовите вашу фамилию: ')
#     day = input('Назовите  вашу дату рождения: ')
#     city = input('Назовите  ваш город проживания: ')
#     mail = input('Назовите  вашу  электронную почту: ')
#     phone = input('Назовите ваш номер тедефона: +7-')
#     return (f'{name} {first_name}. Вы родились {day} в городе {city}. Ваш email: {mail}, телефон: {phone}.')
#
# print(info())

# Задание 3

# def my_func(*args):
#     el_1 = int(input('Ведите число 1: '))
#     el_2 = int(input('Ведите число 2: '))
#     el_3 = int(input('Ведите число 3: '))
#     el = [el_1, el_2, el_3]
#     el.remove(min(el_1, el_2, el_3))
#     return sum(el)
#
# print(my_func())

# Задание 4
"""Не получается поставить большее кол-во знаков после запятой в первом варианте???"""


# def func_4_1(x, y):
#     return 1 // x ** abs(y)
#
#
# print(func_4_1(5, -2))
#
# def func_4_2(x, y):
#     for i in range (abs(y)):
#         x *= x
#     return 1/x
#
# print(func_4_2(5, -2))

# Задание 5

# def sum_numb (*args):
#     number = 0
#     while True:
#         numbers = input('Введите числа через пробел или симввол # для выхода из программы: ').split( )
#         for i in numbers:
#             try:
#                 if i == "#":
#                     print('Вы нажали вызод из программы')
#                     return
#                 else:
#                     number += int(i)
#             except:
#                 print('Введите число или #')
#         print(f'сумма чисел {number}')
#
# print(sum_numb())

# Задание 6.7
''' в 7 задании выдает ошибку не могу понять в чем дело'''

def int_func(text):
    spisok = []
    spisok.append(text [0:1].title() + text [1:])
    return ''.join(spisok)

print(int_func('text'))

def int_func_2 ():
    print(int_func(input('Введите слова через пробел: ').split( )))

print(int_func_2())

