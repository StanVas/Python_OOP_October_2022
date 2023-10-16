def uppercase(func_ref):
    def wrapper():
        func_result = func_ref()
        return func_result.upper()

    return wrapper


@uppercase
def say_hi():
    return "hello world"


@uppercase
def say_bye():
    return "goodbye world"


print(say_hi())
print(say_bye())

say_hi = uppercase(say_hi)
print(say_hi())
print(say_hi)  # return address

x = say_hi
print(x())
print(x.__class__)  # <class 'function'>
print(x.__class__.__name__)  # function
