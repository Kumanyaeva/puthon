# Задание №1

# class Matrix:
#     def __init__(self, my_matr):
#         self.my_matr = my_matr
#     def __str__(self):
#         for el in self.my_matr:
#             for i in el:
#                 print(f"{i:}", end=" ")
#             print()
#         return
#     def __add__(self, other):
#         for el in range(len(self.my_matr)):
#             for i in range(len(self.my_matr[el])):
#                 self.my_matr[el][i] = self.my_matr[el][i] + other.my_matr[el][i]
#         return Matrix.__str__(self)
#
# matrix = Matrix([[5, 3, 1], [-5, 5, 1], [8, 10, -1]])
# new_matrix = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2]])
# # matrix.__str__()
#
# print(matrix.__add__(new_matrix))

# Задание №2

""""Неудается реализовать общий обем такани понимаю что не те элементы но не могу понять от куда брать надо, если задаю вначале 2 элемента,
то потом и на дочерние классы это распространяется"""

# from abc import ABC
#
# class Cloth(ABC):
#     def __init__(self, tkan):
#         self.tkan = tkan
#
# class Coat(Cloth):
#     def all_cloth(self):
#         n = self.tkan // 6.5 + 0.5
#         return print(f'Общий объем для пальто: {n}')
# class Suit(Cloth):
#     def all_cloth(self):
#         b = 2 * self.tkan + 0.3
#         return print(f'Общий объем ткани для костюма: {b}')
#
# coat = Coat(500)
# coat.all_cloth()
#
# suit = Suit(300)
# suit.all_cloth()
#
# print(f'Общий объем ткани: {Coat.all_cloth(500) + Suit.all_cloth(300)}')

# Задание №3

class Cletca:
    def __init__(self, kol_vo):
        self.kol_vo = int(kol_vo)

    def __add__(self, other):
        return f'Две клетки - маленькие, а одна - большая! Размер одной клетки равен: {self.kol_vo + other.kol_vo}'

    def __sub__(self, other):
        sub = self.kol_vo - other.kol_vo
        return f'Клетка стала меньше, и теперь она равна: {sub} клеточкам' if sub > 0 else 'Нет клетки!'

    def __truediv__(self, other):
        return self.kol_vo // other.kol_vo

    def __mul__(self, other):
        return self.kol_vo * other.kol_vo

    def make_order(self, el):
        result = ''
        for i in range(int(self.kol_vo / el)):
            result += '*' * el + '\n'
        result += '*' * (self.kol_vo % el) + '\n'
        return result


cletca = Cletca(24)
cletca_2 = Cletca(2)
print(cletca + cletca_2)
print(cletca - cletca_2)
print(cletca / cletca_2)
print(cletca * cletca_2)
print(cletca.make_order(7))