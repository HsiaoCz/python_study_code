a = 12
b = "hello"
c = False


class Cat:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def hello(self):
        print(f"hello:{self.name}")
