# задача: открываем файл, пишем название, печатаем 2 строки, печатаем позицию, закрываем файл
f = open('test', 'r')
print(f.name)

print(f.readline())
print(f.readline())

print(f.tell())
f.close()
# код ок, но придется копировать если захотим прочитать так же другой файл




# функция, работает, но try except (если вдруг будет ошибка и файл не закроем)
# выглядит плохо
def read(path):
    f = open(path, 'r')
    try:
        print(f.name)

        print(f.readline())
        print(f.readline())

        print(f.tell())
    finally:
        f.close()


read('test')




# контекстный менеджер в виде класса
class FileOpener:

    def __init__(self, file_path):  # конструктор, запомнили путь в self.file_path
        self.file_path = file_path

    def __enter__(self):  # при входе в контекст
        self.file = open(self.file_path, 'r')  # открыли файл, запомнили объект открытого файла в self.file
        print(self.file.name)  # печатаем имя файла
        return self  # возвращаем объект контекстного менеджера в тело контекста

    def read(self):  # функция, печатающий строчку файла
        print(self.file.readline())

    def seek_to_start(self):  # функция, возвращающая позицию чтения в самое начало в первую строку
        self.file.seek(0)

    def __exit__(self, exc_type, exc_val, exc_tb):  # при выходе из контекста
        print(self.file.tell())  # печатаем текущую позицию
        self.file.close()  # закрываем открытый файл


f_opener = FileOpener('test')  # создали контекстный менеджер (вызвался __init__)

# входим в контекст (вызвался __enter__)
with f_opener as test_file:  # в test_file проставился self контекста, напечатали имя файла
    test_file.read()  # печатаем 1 строку
    test_file.read()  # печатаем 2 строку
    test_file.seek_to_start()  # возвращаем позицию чтения в начало файла
    test_file.read()  # печатаем 1 строку
    print(test_file.file.readline())  # печатаем 2 строку напрямую из файла, который доступен через контекст

# вышли из контекста (вызвался __exit__), напечатали текущую позицию, закрыли файл






# контекстный менеджер в виде функции
from contextlib import contextmanager


@contextmanager  # декоратор, превращающий функцию в аналог класса
def file_opener(file_path):
    # все что до yield == __enter__
    f = open(file_path, 'r')
    print(f.name)

    yield f  # аналог return, возвращаем открытый файл f, но сохраняем контекст для возвращения

    # все что после yield == __exit__
    print(f.tell())
    f.close()


with file_opener('test') as f:
    print(f.readline())
    print(f.readline())
