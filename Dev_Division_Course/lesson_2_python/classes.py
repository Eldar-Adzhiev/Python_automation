class Human:
    age = None
    sex = None
    weight = None

    def __getattribute__(self, item):
        print(f'Now i will return {item} of {self}')

    def __setattr__(self, key, value):
        print(f'Now i will set {key}={value} for {self}')

    def __delattr__(self, item):
        print(f'Now i will delete {item} ok {self}')


human1 = Human()
print(human1)  # some id

human2 = Human()
print(human2)  # another id


human1.age = 20  # calls __setattr__
human1.sex = 'M'
human1.weight = 80

human2.age = 18
human2.sex = 'F'
human2.weight = 50

print(human1.age)  # calls __getattribute__
del human2.age     # calls __delattr__


# выводим все атрибуты объекта
print(human1.__dict__)
print(dir(human2))





class Human:
    _age = None  # protected, номинально запрещаем менять за пределами данного класса
    __private_attr = None  # инкапсулировано, нельзя вызывать за пределами данного класса

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._age



human = Human()

# недоступно
# print(human.__private_attr)

print(human.get_age())
human.set_age(18)
print(human.get_age())


# наследуемся от человека, перенимаем все свойства и методы
class Man(Human):
    pass


# наследуемся от человека, перенимаем все свойства и методы, заменяем один из них
class Woman(Human):

    @property
    def get_age(self):
        return self._age - 10


man = Man()
man.set_age(60)
print(man.get_age())

women = Woman()
women.set_age(30)
print(women.get_age)



print(issubclass(Woman, Human))  # True, класс Woman является наследником класса Human
print(isinstance(women, Human))  # True, women является экземпляром человека (так как тип Woman -> наследник Human)
