class Parent:
    def __init__(self):
        self.parent_attribute = 'I am a parent'

    def parent_method(self):
        print('Back in my day...')


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attribute = 'I am a child'


def main() -> None:
    child = Child()

    print(child.child_attribute)
    print(child.parent_attribute)
    child.parent_method()


if __name__ == '__main__':
    main()