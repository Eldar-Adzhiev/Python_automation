import time
from functools import wraps


def timing(f):
    """Decorator for measure the execution time of functions"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # запомнили время до выполнения функции

        result = f(*args, **kwargs)  # выполнили декорируемую функцию, заполнили ее результат

        end_time = time.time()  # получили время после выполнения функции
        print(f"Function {f.__name__} took {end_time - start_time} secs")  # время после - время до == время выполнения
        return result  # возвращаем запомненный результат тому кто вызывал декорируемую функцию

    return wrapper


@timing
def func():
    import random
    import time
    time.sleep(random.randint(0, 10))


func()
func()
func()
