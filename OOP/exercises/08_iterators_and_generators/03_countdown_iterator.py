class countdown_iterator:
    def __init__(self, count: int):
        self.count = count + 1
        self.counter = self.count

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= 0:
            raise StopIteration

        self.counter -= 1

        return self.counter


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
