# Задание_1

# class Data:
#     # def __init__(self, day = str, month = str, year = str):
#     #     self.day = day
#     #     self.month = month
#     #     self.year = year
#     def __init__(self, day_month_year = str):
#         self.day_month_year = day_month_year
#
#     @classmethod
#     def number (cls, day_month_year):
#         date_numb = []
#
#         for i in day_month_year.split():
#             if i != '-': date_numb.append(i)
#
#         return int(date_numb[0]), int(date_numb[1]), int(date_numb[2])
#
#
#     @staticmethod
#     def valid(day, month, year):
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2022 >= year >= 0:
#                     return f'True'
#                 else:
#                     return f'Неправильный год'
#             else:
#                 return f'Неправильный месяц'
#         else:
#             return f'Неправильный день'
#
#
#     def __str__(self):
#         return f'Текущая дата {Data.number(self.day_month_year)}'
#
#
# data = Data('10 - 4 - 2022')
# print(data)
# print(Data.valid(30, 11, 2020))
# print(data.valid(15, 12, 1821))
# print(Data.number('10 - 4 - 2022'))
# print(data.number('10 - 4 - 2022'))
# print(Data.valid(30, 11, 2020))

# Задание_2

"""" не уверена в правильности реализации"""

# import traceback
#
# class deli_na_nol(Exception):
#     def __init__(self, chislitel, znamenatel):
#         self.chislit = chislitel
#         self.znam = znamenatel
#
#     def del_nul_not(chislitel, znamenatel):
#         try:
#             return (chislitel // znamenatel)
#             if znamenatel == 0:
#                 return (f'Делить на ноль нельзя!!!')
#         except deli_na_nol as err:
#             print('Ошибка:', traceback.format_exc())
#
#
# n = deli_na_nol(1, 1)
# print(deli_na_nol.del_nul_not(100, 10))
# print(deli_na_nol.del_nul_not(100, 0))

# Задание_3

# class Error_my:
#     def __init__(self, *args):
#         self.my_list = []
#
#     def my_input(self):
#
#         while True:
#             try:
#                 val = int(input('Введите значения и нажимайте Enter: '))
#                 self.my_list.append(val)
#                 print(f'Текущий список - {self.my_list} \n ')
#             except:
#                 if val == str:
#                     print('')
#                 else:
#                     print(f"Недопустимое значение - строка")
#                     return f'Вы вышли'
#
#
# try_except = Error_my()
# print(try_except.my_input())

# Задание_4,5,6

# class Stock:
#
#     def __init__(self, name, price, amount,  *args):
#         self.name = name
#         self.price = price
#         self.amount = amount
#         self.my_stock_oll = []
#         self.my_stock = []
#         self.my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.amount}
#
#     def __str__(self):
#         return f'{self.name} цена {self.price} количество {self.amount}'
#
#     def reception(self):
#         try:
#             unit = input(f'Введите наименование ')
#             unit_p = int(input(f'Введите цену за ед '))
#             unit_q = int(input(f'Введите количество '))
#             unique = {'Модель устройства': {unit}, 'Цена за ед': {unit_p}, 'Количество': {unit_q}}
#             self.my_unit.update(unique)
#             self.my_stock.append(self.my_unit)
#             print(f'Текущий список -\n {self.my_stock}')
#         except:
#             return f'Ошибка ввода данных'
#
# class Printer(Stock):
#     def print_my(self):
#         return f'Принтеры {self.name}'
#
#
# class Scanner(Stock):
#     def scan(self):
#         return f'Сканеры: {self.name}'
#
#
# class Copier(Stock):
#     def copier_my(self):
#         return f' Копи машины: {self.name}'
#
#
# unit_1 = Printer('hp', 2000, 5, 10)
# unit_2 = Scanner('Canon', 1200, 5, 10)
# unit_3 = Copier('Xerox', 1500, 1, 15)
# print(unit_1.reception())
# print(unit_2.reception())
# print(unit_3.reception())
# print(unit_1.print_my())
# print(unit_2.scan())
# print(unit_3.copier_my())

# Задание_7

class Complex_number:
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        self.z = 'x + y * i'

    def __add__(self, other):
        print(f'Сумма z_1 и z_2 равна')
        return f'z_0 = {self.x + other.x} + {self.y + other.y} * i'

    def __mul__(self, other):
        print(f'Произведение z_1 и z_2 равно')
        return f'z_0 = {self.x * other.x - (self.y * other.y)} + {self.y * other.y} * i'

    def __str__(self):
        return f'z_0 = {self.x} + {self.y} * i'


z_1 = Complex_number(5, -3)
z_2 = Complex_number(10, 5)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)