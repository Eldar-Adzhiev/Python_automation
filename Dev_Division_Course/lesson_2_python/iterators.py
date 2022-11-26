num_list = [1, 2, 3, 4, 5]

itr = iter(num_list)  # создаем итератор

print(next(itr))  # следующее значение - 1
print(next(itr))  # следующее значение - 2
print(next(itr))  # следующее значение - 3
print(next(itr))  # следующее значение - 4
print(next(itr))  # следующее значение - 5

print(next(itr))  # cписок кончился, выбрасывается исключение StopIteration


# for останавливается на StopIteration
for i in num_list:
    print(i)





# итератор в разрезе в виде класса
class SimpleIterator:

    def __init__(self, limit):  # конструктор, задаем лимит
        self.limit = limit
        self.counter = 0  # счетчик итератора выставляем в 0

    def __iter__(self):  # объявляем класс итератором
        return self

    def __next__(self):  # объявляем метод, выдающий следующее значение
        if self.counter < self.limit:  # пока счетчик не превысил лимит -> увеличиваем счетчик
            self.counter += 1
            return self.counter  # возвращаем счетчик
        else:
            # выбрасываем исключение, когда счетчик превысил лимит -> останавливаем итерацию для for
            raise StopIteration


s_iter = SimpleIterator(5)
for i in s_iter:
    print(i)

print(s_iter.counter)
