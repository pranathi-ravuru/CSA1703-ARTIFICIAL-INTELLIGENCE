# Water Jug Problem

a = 0
b = 0

print("Initial State: (0, 0)")

# Fill Jug 2
b = 3
print("Fill Jug 2:", a, b)

# Pour Jug 2 into Jug 1
a = b
b = 0
print("Pour Jug 2 into Jug 1:", a, b)

# Fill Jug 2 again
b = 3
print("Fill Jug 2:", a, b)

# Pour Jug 2 into Jug 1
b = b - (5 - a)
a = 5
print("Pour Jug 2 into Jug 1:", a, b)

# Empty Jug 1
a = 0
print("Empty Jug 1:", a, b)

# Pour Jug 2 into Jug 1
a = b
b = 0
print("Pour Jug 2 into Jug 1:", a, b)

if a == 1:
    print("Goal achieved!")
