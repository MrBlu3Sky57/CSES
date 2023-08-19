import numpy as np

num_paths = 0
T = 7
N = 9
R = np.array([1, 0])
L = np.array([-1, 0])
U = np.array([0, -1])
D = np.array([0, 1])
moves = {"R": R, "L": L, "U": U, "D": D}

input_taken = np.zeros([N, N], dtype=bool) # Initialize Grid

# Pad Grid
for x in range(N):
    for y in range(N):
        if x == N - 1 or y == N - 1 or x == 0 or y == 0:
            input_taken[x][y] = True
input_taken[1][1] = True

string = list(input())
        
def solve(idx, taken, cur):
    global num_paths
    # print(idx)
    # print(cur)
    # Check for grid splitting
    if taken[cur[0] + 1][cur[1]] == True and taken[cur[0] - 1][cur[1]] == True and taken[cur[0]][cur[1] + 1] == False and taken[cur[0]][cur[1] - 1] == False:
        return 0
    if taken[cur[0]][cur[1] + 1] == True and taken[cur[0]][cur[1] - 1] == True and taken[cur[0] + 1][cur[1]] == False and taken[cur[0] - 1][cur[1]] == False:
        return 0
    
    # Check for valid path
    if cur[0] == 1 and cur[1] == T:
        if idx == 48:
            num_paths += 1
            return 1
        # print("early_finish")
        return 0

    if idx == 48:
        # print("Wrong endpoint")
        return 0

    if string[idx] != "?":
        attempt = moves[string[idx]] + cur 

        if taken[attempt[0]][attempt[1]] == True:
            # print("Place is taken")
            return 0
        else:
            new_taken = np.copy(taken)
            new_taken[attempt[0]][attempt[1]] = True
            solve(idx + 1, new_taken, attempt)
    elif cur[0] < 6 and taken[cur[0] + R[0]][cur[1] + R[1]] == False and (taken[cur[0] + R[0] + U[0]][cur[1] + R[1] + U[1]] == True or taken[cur[0] + R[0] + D[0]][cur[1] + R[1] + D[1]] == True) and taken[cur[0] + 2 * R[0]][cur[1] + 2 * R[1]] == True:
                move = cur + R
                new_taken = np.copy(taken)
                new_taken[move[0]][move[1]] = True
                solve(idx + 1, new_taken, move)
    elif cur[0] > 2 and taken[cur[0] + L[0]][cur[1] + L[1]] == False and (taken[cur[0] + L[0] + U[0]][cur[1] + L[1] + U[1]] == True or taken[cur[0] + L[0] + D[0]][cur[1] + L[1] + D[1]] == True) and taken[cur[0] + 2 * L[0]][cur[1] + 2 * L[1]] == True:
                move = cur + L
                new_taken = np.copy(taken)
                new_taken[move[0]][move[1]] = True
                solve(idx + 1, new_taken, move)
    elif cur[1] > 2 and taken[cur[0] + U[0]][cur[1] + U[1]] == False and (taken[cur[0] + U[0] + L[0]][cur[1] + U[1] + L[1]] == True or taken[cur[0] + U[0] + R[0]][cur[1] + U[1] + R[1]] == True) and taken[cur[0] + 2 * U[0]][cur[1] + 2 * U[1]] == True:
                move = cur + U
                new_taken = np.copy(taken)
                new_taken[move[0]][move[1]] = True
                solve(idx + 1, new_taken, move)
    elif cur[1] > 6 and taken[cur[0] + D[0]][cur[1] + D[1]] == False and (taken[cur[0] + D[0] + L[0]][cur[1] + D[1] + L[1]] == True or taken[cur[0] + D[0] + R[0]][cur[1] + D[1] + R[1]] == True) and taken[cur[0] + 2 * D[0]][cur[1] + 2 * D[1]] == True:
                move = cur + D
                new_taken = np.copy(taken)
                new_taken[move[0]][move[1]] = True
                solve(idx + 1, new_taken, move)
    else:
        for x in moves.values():
            attempt = x + cur
            if taken[attempt[0]][attempt[1]] == False:
                new_taken = np.copy(taken)
                new_taken[attempt[0]][attempt[1]] = True
                # print("not forced")
                solve(idx + 1, new_taken, attempt)



solve(0, input_taken, np.array([1, 1]))
print(num_paths)