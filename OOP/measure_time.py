from time import time

start = time()

print("Write this text:")
print("Another top-notch Python cheat sheet is Website Setup,"
      " which ranks right below Pythoncheatsheet.org in terms of popularity.")

text = input()

end = time()

print(end - start)


# def measure_time(func):
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         end = time()
#         print(end - start)
#         return result
#     return wrapper()