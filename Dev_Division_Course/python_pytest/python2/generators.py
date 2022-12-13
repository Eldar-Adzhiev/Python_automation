def simple_generator(val):
    while val > 0:  # до тех пор пока значение val > 0 - отдаем единицы
        val -= 1  # на каждую итерацию уменьшаем значение val
        yield 1  # возвращаем 1, но сохраняем контекст и значение val



gen_iter = simple_generator(5)

print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))
print(next(gen_iter))


for i in gen_iter:
    print(i)





# задача - прочитать очень большой файл и вывести содержимое на экран
f = open('test', 'r')  # 100Gb
print(f.read())  # не хватит памяти, падаем
f.close()


# open может быть использован как контекстный менеджер
with open('test', 'rb') as f:  # в f попадет объект открытого файла. флаг 'b' - откроет файл в бинарном формате
    for line in f:  # объект открытого файла является генератором, позволяющий итерироваться по строкам файла
        print(line)  # построчно читаем каждую новую строчку до тех пор пока файл не кончится
