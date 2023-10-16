def squares(num: int):
    counter = 0

    while counter < num:
        counter += 1
        yield counter ** 2


print(list(squares(5)))
