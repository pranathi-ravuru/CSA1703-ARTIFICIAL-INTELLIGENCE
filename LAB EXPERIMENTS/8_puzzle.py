# 8 Puzzle Problem

start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

moves = 0

print("Initial State:")
print(start[0:3])
print(start[3:6])
print(start[6:9])

# Move 1: Move 5 up
start[4], start[7] = start[7], start[4]
moves += 1

print("\nMove", moves)
print(start[0:3])
print(start[3:6])
print(start[6:9])

# Move 2: Move 8 left
start[7], start[8] = start[8], start[7]
moves += 1

print("\nMove", moves)
print(start[0:3])
print(start[3:6])
print(start[6:9])

if start == goal:
    print("\nPuzzle Solved!")
    print("Total Moves =", moves)
else:
    print("\nPuzzle Not Solved")
