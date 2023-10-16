class Parent:
    pass


class FirstChild(Parent):
    pass


class SecondChild(Parent):
    pass


class GrandChild(SecondChild, FirstChild):
    pass


print(GrandChild.mro())
# mro = method resolution order
