# from collections import deque
#
#
# class sequence_repeat:
#     def __init__(self, sequence: str, number: int):
#         self.sequence = deque(sequence)
#         self.number = number
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.counter >= self.number:
#             raise StopIteration
#
#         self.counter += 1
#         result = self.sequence.popleft()
#         self.sequence.append(result)
#
#         return result
#
#
# result = sequence_repeat('abc', 5)
# for item in result:
#     print(item, end='')
#
# result = sequence_repeat('I Love Python', 3)
# for item in result:
#     print(item, end='')

# from the lection

class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.number - 1:
            raise StopIteration

        self.idx += 1

        return self.sequence[self.idx % len(self.sequence)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
