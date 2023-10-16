class reverse_iter:
    def __init__(self, some_iterable):
        self.some_iterable = some_iterable

    def __iter__(self):
        return self

    def __next__(self):
        if not self.some_iterable:
            raise StopIteration()

        return self.some_iterable.pop()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
