import colorama
from colorama import Fore,Back, Style
class Vehicle():
    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__color = str(__color)
        self.__engine_power = int(__engine_power)
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def get_model(self):
        print(Fore.BLUE + f'Модель: {self.__model}')
    def get_color(self):
        print(Fore.BLUE + f'Цвет: {self.__color.upper()}')
    def get_horsepower(self):
        print(Fore.BLUE + f'Мощность двигателя: {self.__engine_power}')

    def print_info(self):
        self.get_model()
        self.get_color()
        self.get_horsepower()
        print(Fore.BLUE + "Владелец: " + self.owner)
    def set_color(self, new_color):
        k = 0
        for i in self.__COLOR_VARIANTS:
            if i.upper() == str(new_color).upper():
                self.__color = str(new_color)
                k = 1
                break
        if k == 0:
            print(Fore.RED + "Нельзя сменить цвет на " + Fore.GREEN + new_color)
class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5
# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

