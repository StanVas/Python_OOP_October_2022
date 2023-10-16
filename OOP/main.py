# # name mangling
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#
# person = Person('Gosho', 18)
# print(person._Person__age)
class ToyStore:
    def __init__(self):
        self.toy_shelf = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }


toy_store = ToyStore()
print(toy_store.toy_shelf)

s = 'python'
print(s + s[::-1])