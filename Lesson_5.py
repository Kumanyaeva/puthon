#Задание 1
'''я вроде расставила \n - символы но перенос не получается'''

# with open("text.txt", "w", encoding='Utf-8') as f_obj:
#     line = input('Введите параметры: \n')
#     while line:
#         f_obj.writelines(line)
#         line = input('Введите параметры: \n')
#         if not line:
#             break

# with open("text.txt", "r", encoding='Utf-8') as f_obj:
#     content = f_obj.readline()
#     print(content)

#Задание 2
from typing import List, Any, Dict

""" кол-во слов не смогла реализовать """

# with open("text_2.txt", "r", encoding='Utf-8') as f_obj_2:
#     content = f_obj_2.readlines()
#     print(f'Количество строк в файле - {len(content)}')

#Задание 3

# with open('text_3.txt', 'r', encoding='Utf-8') as my_file:
#     salary = []
#     staf = []
#     my_list = my_file.read().split("\n")
#     for i in my_list:
#         i = i.split()
#         if int(i[1]) < 20000:
#            staf.append(i[0])
#         salary.append(i[1])
# print(f'Оклад меньше 20.000 {staf}, средний оклад {sum(map(int, salary)) / len(salary)}')

#Задание 4

# dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
# my_list = []
# with open('text_4.txt', 'r', encoding='utf-8') as my_file_4:
#     for i in my_file_4:
#         i = i.split(' ', 1)
#         my_list.append(dict[i[0]] + '  ' + i[1])
#     print(my_list)
#
# with open("text_4_rus.txt", "w", encoding='utf-8') as my_file_4_2:
#     cont = my_file_4_2.writelines(my_list)

#Задание 5
import math

# def summa ():
#     try:
#         with open ('text_5.txt', 'w', encoding='utf-8') as f_obj:
#             number = input('Введите числа через пробулы и поставьте Enter: ')
#             f_obj.writelines(number)
#             my_number = number.split()
#             print(sum(map(int, my_number)))
#     except:
#         print('Ошибка')
# print(summa())

#Задание 6

# """Я не знала как делать правила в файле, не смогла разобраться ((("""
# subj = {}
#
# with open('text_6.txt', 'r', encoding='utf-8') as f_obj:
#     for line in f_obj:
#         subject, lect, pract, lab = line.split()
#         subj[subject] = int(lect) + int(pract) + int(lab)
#         print(subj)

#Задание 7

import json


prib = {}
pr = {}
prof = 0
prof_sr = 0
i = 0
with open('text_7.txt', 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        name, firm, earning, damage = line.split()
        prib[name] = int(earning) - int(damage)
        if prib.setdefault(name) >= 0:
            prof = prof + prib.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль средняя - нет. Все работают в убыток')
    pr = {'средняя прибыль': round(prof_aver)}
    prib.update(pr)
    print(f'Прибыль каждой компании - {prib}')

with open('text_7.json', 'w', encoding='utf-8') as write_js:
    json.dump(prib, write_js)

    js_str = json.dumps(prib)
    print(f'Создаем файл с расширением json: \n '
          f' {js_str}')