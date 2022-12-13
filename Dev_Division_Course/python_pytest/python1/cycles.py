lst = [1, 2, 3, 4, 5]


cnt = 0  # глобальный счетчик
for i in lst:  # итерируемся по списку, в i проставляется значение на каждой итерации
    if i == 2:
        continue  # пропускаем данную итерацию, принудительно переходим к следующей

    if i == 4:
        break  # останавливаем цикл

    print(i)
    cnt += 1

print(cnt)


import time

started = time.time()
while time.time() - started <= 5:  # пока не наступил таймут 5с: выполняем цикл
    if time.time() - started > 3:
        break  # принудительно прерываем если уже превысили 3 секунды цикла

    print('Waiting')
    time.sleep(1)


i = 0
while True:  # бесконечный цикл, всегда предусматриваем 100% момент выхода
    i += 1
    if i > 5:
        break





