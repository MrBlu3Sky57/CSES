num_paths = 0
N = 7 # Grid Size
M = 0 # Grid Start

input = list(input())

def solve(coordinates, move_number):
    global num_paths
    if N in coordinates or (M - 1) in coordinates:
        if coordinates == [N, N]:
            num_paths += 1
    else:
        next_move = input[move_number]
        if next_move == "R":
            coordinates[0] += 1
            solve(coordinates, move_number + 1)
        elif next_move == "L":
            coordinates[0] -= 1
            solve(coordinates, move_number + 1)
        elif next_move == "U":
            coordinates[1] += 1
            solve(coordinates, move_number + 1)
        elif next_move == "D":
            coordinates[1] -= 1
            solve(coordinates, move_number + 1)
        else:
            coordinates[0] += 1
            solve(coordinates, move_number + 1)
            coordinates[0] -= 2
            solve(coordinates, move_number + 1)
            coordinates[0] += 1
            
            coordinates[1] += 1
            solve(coordinates, move_number + 1)
            coordinates[1] -= 2
            solve(coordinates, move_number + 1)
            coordinates[1] += 1

print(num_paths)