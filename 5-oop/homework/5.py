class MyClass:
    def __init__(self, attr1, attr2, attr3):
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3

    def __setattr__(self, key, value):    # вызыывается при установке новых атрибутов, в т.ч. в __init__
        if hasattr(self, key):
            print(f'__setattr__: {getattr(self, key)} -> {value}')
        object.__setattr__(self, key, value)


def main() -> None:
    my_object = MyClass(1, 2,3)
    my_object.attr1 = 30
    my_object.attr2 = 65


if __name__ == '__main__':
    main()