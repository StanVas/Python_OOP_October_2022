x = 'global'


def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'  # changing line 5(in the scope of def outer)
        print("inner:", x)

    def change_global():
        global x  # changing line 1
        x = 'global: changed!'

    print('outer:', x)
    inner()
    print('outer:', x)
    change_global()


print(x)
outer()
print(x)
