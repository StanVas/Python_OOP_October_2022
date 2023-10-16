def genrange(start: int, end: int):

    while start < end + 1:
        yield start
        start += 1


print(list(genrange(1, 10)))
