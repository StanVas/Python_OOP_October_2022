def draw_fig(num):
    for row in range(1, num + 1):
        print_row(num, row)

    for row in range(num - 1, -1, -1):
        print_row(num, row)


def print_row(fig_size, row_size):
    print(' ' * (fig_size - row_size), end="")
    for _ in range(1, row_size + 1):
        print('* ', end='')
    print()


number = int(input())

draw_fig(number)
