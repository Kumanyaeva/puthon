# Задание №1

# from itertools import cycle
# from time import sleep
#
# class TrafficLight:
#     __color = cycle([
#         {'signal': 'красный', 'time': 7},
#         {'signal': 'желтый', 'time': 2},
#         {'signal': 'зеленый', 'time': 5}])
#     def running(self):
#         light = next(self.__color)
#         print(f"Сигнал сфетофора {light['signal']}, пауза длинною {light['time']} сек.")
#         sleep(light['time'])
#
# traf_light = TrafficLight()
# traf_light.running()
# traf_light.running()
# traf_light.running()
# traf_light.running()

# Задание №2
from turtle import width


# class Road:
#     def __init__(self, length = int, width = int):
#         self._length = length
#         self._width = width
#     def asf_mass (self, mass_1m2 = int, thickness = int):
#         mass = self._length * self._width * mass_1m2 * thickness//1000
#         return mass
# road = Road(5000, 20)
# print(road.asf_mass(25, 5))

# Задание №3

# class Worker:
#     def __init__(self, name = str, surname= str, position= str, wage = int, bonus = int):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}
#
# class Position (Worker):
#     def get_full_name (self):
#         print(f"Полное имя сотрудника: {self.name} {self.surname}")
#     def get_total_income (self):
#         print(f"Заработная плата сотрудника с учетом премии: {sum(self._income.values())} руб.")
#
# pos_1 = Position ('Ирина', 'Куманяева','Аналитик', 100000, 20000)
# pos_1.get_full_name()
# print(pos_1.position)
# pos_1.get_total_income()

# Задание №4

# class Car:
#     def __init__(self, speed, color, name, is_police: bool):
#         self.speed = 0
#         self.color = color
#         self.name = name
#         self.is_polise = is_police
#         print(f"Это {color} {name}")
#     def go (self, speed):
#         self.speed = speed
#         print(f"Мы едем со скоростью {speed} км/ч")
#
#     def stop(self):
#         self.speed = 0
#         print('Останавливаемся')
#
#     def turn(self, direction):
#         if self.speed > 0:
#             print(f'Поворачиваем {direction}')
#         else:
#             print('Ничего не делай!!!')
#     def show_speed(self):
#         print(f'Скорость автомобиля сейчас: {self.speed} км/ч')
#
# class TownCar(Car):
#     def __init__(self, color, name):
#         self.speed = 0
#         self.color = color
#         self.name = name
#         self.is_police = False
#         print(f"Это {color} {name}")
#
#     def show_speed(self):
#         if self.speed > 60:
#             print(f'Внимание!!! Превышение скорости {self.speed} км/ч. Сбросьте скорость до 60 км/ч')
#         else:
#             print(f'Скорость {self.speed} км/ч, вы можете продолжать движение')
#
#
# class SportCar(Car):
#     def __init__(self, color, name):
#         self.speed = 0
#         self.color = color
#         self.name = name
#         self.is_police = False
#         print(f"Это {color} {name}")
#
#
# class WorkCar(Car):
#     def __init__(self, color, name):
#         self.speed = 0
#         self.color = color
#         self.name = name
#         self.is_police = False
#         print(f"Это {color} {name}")
#
#     def show_speed(self):
#         if self.speed > 40:
#             print(f'Внимание!!! Превышение скорости {self.speed} км/ч. Сбросьте скорость до 40 км/ч')
#         else:
#             print(f'Скорость {self.speed} км/ч, вы можете продолжать движение')
#
#
# class PoliceCar(Car):
#     def __init__(self, color, name):
#         self.speed = 0
#         self.color = color
#         self.name = name
#         self.is_police = True
#         print(f"Это {color} {name} и это полиция!!!")
#
# car = Car (40, 'черный', 'Mersedes', False)
# car.go(60)
# car.turn('направо')
# car.stop()
# car.show_speed()
#
# town_car = TownCar ('белый', 'Mazda')
# town_car.go(90)
# town_car.turn('налево')
# town_car.show_speed()
# town_car.go(50)
# town_car.show_speed()
# town_car.stop()
#
# sport_car = SportCar ('розовый', 'Mazerty')
# sport_car.go(120)
# sport_car.turn('направо')
# sport_car.show_speed()
# sport_car.stop()
#
# work_car = WorkCar ('серый', 'Приора')
# work_car.go(90)
# work_car.turn('направо')
# work_car.show_speed()
# work_car.go(30)
# work_car.show_speed()
# work_car.stop()
#
# poloce_car = PoliceCar ('голубая', 'Волга')
# poloce_car.go(60)
# poloce_car.turn('направо')
# poloce_car.show_speed()
# poloce_car.stop()

# Задание №5

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'Запуск отрисовк {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовк ручкой {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовк карандашом {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовк маркером {self.title}')

stationery = Stationery ('красками')
stationery.draw()
pen = Pen ('шариковой')
pen.draw()
pencil = Pencil ('с твердым грифилем')
pencil.draw()
hand = Handle ('красным')
hand.draw()