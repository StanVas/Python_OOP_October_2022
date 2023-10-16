class MyClass:
    def __repr__(self):  # machine readable representation
        return 'This is My Class'


my_instance = MyClass()

print(repr(my_instance))
print(my_instance.__repr__())
print(my_instance)
