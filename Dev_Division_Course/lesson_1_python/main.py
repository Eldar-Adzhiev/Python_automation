# переменные

# valid:
num = 1
num35num35 = 1
first_num = 1
my_var = 111
var_111_ = 111


# invalid:
# 1num = 1


del num  # удаляем переменную, со временем garbage collector удалит объект из памяти


_var = 1   # protected переменная, запрещаем менять
__var = 1  # private переменные, запрещаем использовать вне данного контекста


# swap переменных
x = 1
y = 2
x, y = y, x
# x = 2, y = 1


# распаковка списка
lst1 = [1, 2, 3, 4, 5]
a, b, c, d, e = lst1
print(a, b, c, d, e)


# распаковка кортежей (ключ, значение) в цикле
di = {1: 1, 2: 2, 3: 3}
for k, v in di.items():
    print(k, v)


# распаковка списка
print(*lst1, sep=', ')
print(a, b, c, d, e)


# распаковка словаря
date = {'year': 1999, 'month': 12, 'day': 31}
filename = '{year}-{month}-{day}'.format(**date)
filename1 = '{year}-{month}-{day}'.format(year=1999, month=12, day=31)


filename2 = f'{date["year"]}-{date["month"]}-{date["day"]}'
print(filename)
print(filename1)
print(filename2)


# if elif else
welcome_str = None
if welcome_str is None:
    welcome_str = "hello, system, this is <Mary>"


if 'Nick' in welcome_str:
    print('This is Nick')
elif 'Mary' in welcome_str:
    print('This is Mary')
else:
    print('Unknown person')



# walrus operator example (python3.8+)
a = [1, 2, 3, 4, 5]
length = len(a)
if length > 3:
    print('LONG')
    print(length)
# 5 строк, 1 вызов len()


a = [1, 2, 3, 4, 5]
if len(a) > 3:
    print('LONG')
    print(len(a))
# 4 строки, 2 вызов len()


a = [1, 2, 3, 4, 5]
if (length := len(a)) > 3:  # присваиваем результат len(a) в переменную length на лету
    print('LONG')
    print(length)
# 4 строки, 1 вызов len()


# match case example (python3.10+)
var = 11111

if var == 123:
    print('123')
elif var == 456:
    print('not 456')
else:
    print('dont know')


match var:
    case 123:
        print('123')
    case 456:
        print('456')
    case _:
        print('dont know')
