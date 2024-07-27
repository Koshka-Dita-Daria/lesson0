
class House:
    houses_history = []
    def __new__(cls, *args, **kwards):
        h_name = args[0] if args else "No name"
        obj = super().__new__(cls)
        cls.houses_history.append(h_name)
        return obj

    def __init__(self, name, numbers_of_floor):
        self.name = name
        self.numbers_of_floor = numbers_of_floor
    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
