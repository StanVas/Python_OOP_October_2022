x = int(input())
y = int(input())
z = int(input())
n = int(input())

X, Y, Z, N = x, y, z, n
result = [[x, y, z] for x in range(X + 1) for y in range(Y + 1) for z in range(Z + 1) if x+y+z != N]

print(result)
