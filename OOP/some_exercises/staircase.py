# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
def staircase(num: int):
    for n in range(1, num + 1):
        print(" " * (num - n) + ('#' * n))


number = int(input())

staircase(number)
