class MyClass:
    class_variable = 1

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable


first = MyClass(2)
second = MyClass(3)

print(MyClass.__dict__)  # {'__module__': '__main__', ...}
print(first.__dict__)  # {'instance_variable': '2'}
print(second.__dict__)

third = MyClass(4).__dict__
print(third["instance_variable"])  # third = dictionary and [instance_variable] = key, so it gives back the value
print(third)  # third = dictionary , so it gives back all keys and values in the dict
