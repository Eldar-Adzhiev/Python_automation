import traceback


try:
    a = int(input('Enter a:'))
    b = int(input('Enter b:'))
    print(a // b)
except ValueError:  # ввели не число и упали на операции int()
    print('Invalid enter')

except ZeroDivisionError:  # второе число оказалось 0
    traceback.print_exc()  # печатаем трассировку ошибки, но не падаем
    print('Zero division')

except:  # перехватываем все остальные случаи
    print('SOMETHING VERY BAD')
    raise Exception('failing')  # сами выбрасываем исключение со своим сообщением, завершаем программу с ошибкой

finally:  # выполнится всегда, независимо возникали ли исключения или нет
    print('Executes always at the end')


print('continue')
