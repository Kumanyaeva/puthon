# задание 1

# spisok = [1, 1.5, 1/5, 'hello']
#
# print(type(spisok[0]))
# print(type(spisok[1]))
# print(type(spisok[2]))
# print(type(spisok[3]))

# задание 2
# list = input('Введите числа в список через запятую: ').split(',')
# list[:-1:2], list[1::2] = list[1::2], list[:-1:2]
#
# print(list)

# задание 3
# dict_1 = {'1' : "зима",
#           '2' : 'зима',
#           '3' : "весна",
#           '4' : "весна",
#           '5' : "весна",
#           '6' : "лето",
#           '7' : "лето",
#           '8' : "лето",
#           '9' : "осень",
#           '10' : "осень",
#           '11' : "осень",
#           '12' : "зима",}
#
# n = input('Введите интересующий Вас месяц: ')
#
# print(f'{n} месяц - это {dict_1[n]}')

# задание 4

# s_1 = input('Введите несколько слов через пробел: ').split(' ')
# for ind, el in enumerate(s_1, 1):
#     print(ind, el[:10])

# задание 5 - я не смогла реализвать функцию чтобы чтобы элемент вставвал в нужное место.

# my_list = [7, 5, 3, 3, 2]
# new_list  = []
#
# for i in my_list:
#     my_list.append(int(input('Введите число: ')))
#
# print(my_list)

# задание 6 не поняла какой функцие надо воспользоваться


product_1 = {'название': '', 'цена': '', 'количество': '', 'ед. изменения': ''}
product_2 = {'название': '', 'цена': '', 'количество': '', 'ед. изменения': ''}

list_product = (product_1, product_2)

product_1 ['название'] = input('Введите название предмета 1: ')
product_1 ['цена'] = int(input('Введите цену предмета 1: '))
product_1 ['количество'] = int(input('Введите количество предмета 1 на остатке: '))
product_1 ['ед. изменения'] = input('Введите ед. в которых измеряется предмет 1: ')

print(product_1)

product_2 ['название'] = input('Введите название предмета 2: ')
product_2 ['цена'] = int(input('Введите цену предмета 2: '))
product_2 ['количество'] = int(input('Введите количество предмета 2 на остатке: '))
product_2 ['ед. изменения'] = input('Введите ед. в которых измеряется предмет 2: ')

print(product_2)


print(list_product(product_1.setdefault('название'), product_2.setdefault('название')))
