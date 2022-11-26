my_str = '12345'

# изменяем строку -> создаем новый объект
my_str += '6'
my_str = my_str + '6'

# способ задания строк
my_str1 = '1234'
my_str2 = "1234"
my_str3 = 'эта строка содержит строку в двойных кавычках: "123"'
my_multiline_str = """
321321
dsadmksla
vcnxklvnxkcl
"""
my_raw_str = r'123\n456'  # игнорируем спецсимволы (\r \n), используем все символы как есть


string = 'hello world'

string.count('l')  # 3
string.capitalize()  # 'Hello world'
string.isdigit()  # False

splitted = string.split(' ')  # получаем список строк ["hello", "world"]


'hello' in 'hello world'  # True
'Hello'.lower() in 'hello world'  # True


# итерируемся по строке
for i in 'hello':
    print(i, end='')


# строки обладают некоторыми свойствами списков
s = '1234567890'
s[0]   # 1
s[-1]  # 0
s[::-1]  # '0987654321'
len(s)  # 10


# форматирование строк
a = '1'
b = '2'
c = '3'

old_string = 'This is a <%s>, this is b <%s>, this is c <%s>' % (a, b, c)
string_format = 'This is a <{}>, this is b <{}>, this is c <{}>'.format(a, b, c)
fstring = f'This is a <{a}>, this is b <{b}>, this is c <{c}>'

print(old_string)
print(string_format)
print(fstring)


bool('')  # False
bool('!!!!')  # True













