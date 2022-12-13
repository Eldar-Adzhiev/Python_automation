from contextlib import contextmanager


@contextmanager
def context(name):
    print(f"Привет, {name}!")
    yield name.upper()
    print(f"Пока, {name}!")


with context("Илья") as name:
    for letter in name:
        print(letter * 3)











class Context:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print(f"Привет, {self.name}!")
        return self

    def print_upper(self):
        for letter in self.name:
            print(letter.upper() * 3)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Пока, {self.name}!")



with Context("Илья") as ctx:
    ctx.print_upper()
