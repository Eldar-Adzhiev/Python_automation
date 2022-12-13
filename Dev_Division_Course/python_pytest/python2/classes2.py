class PlanetClass:
    count = 0                  # атрибут класса

    def __init__(self, name):  # конструктор, принимает аргументы
        self.name = name       # атрибут экземпляра

    def __repr__(self):        # как будет отображаться объект на print()
        return f'Name: "{self.name}"\nCount: {self.count}'

    def __int__(self):         # что будет отображаться на int()
        return self.count

    def __str__(self):         # что будет отображаться на str()
        return f'Счетчик: {self.count}'


planet_1 = PlanetClass('Земля')  # создаем экземпляр класса, передаем имя, count планеты Земля равен 0
planet_1.count += 1              # инкрементируем атрибут экземпляра "земля", count планеты Земля равен 1

PlanetClass.count += 2           # глобально инкрементируем атрибут класса, для всех новых экземпляров он будет равен 2

planet_2 = PlanetClass('Марс')   # создаем экземпляр класса, передаем имя, count планеты Марс равен 2
planet_2.count += 1              # инкрементируем атрибут экземпляра "марс", count планеты Марс равен 3



print(planet_1.count)
print(planet_2.count)


print(planet_2.name)
print(planet_2)


print(int(planet_1))
print(str(planet_1))
