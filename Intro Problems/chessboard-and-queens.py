blocked = []
grid = []

N = 8
# x is the row number and y is the column number
for x in range(N):
        grid.append(list(input()))
        for y in range(len(grid[x])):
            if grid[x][y] == "*":
                blocked.append((x, y))

base_diag1 = [False] * (2 * N - 1)
base_diag2 = [False] * (2 * N - 1)
base_columns = [False] * N

solution_number = 0
def solve(diag1, diag2, columns, row_number):
    global solution_number
    if row_number == N:
        solution_number += 1
        return True
    for x in range(N):
        diag1_index = x + row_number
        diag2_index = row_number + (N - 1) - x
        if columns[x] == False and diag1[diag1_index] == False and diag2[diag2_index] == False and (row_number, x) not in blocked:
            columns[x] = True
            diag1[diag1_index] = True
            diag2[diag2_index] = True
            solve(diag1, diag2, columns, row_number + 1)
            columns[x] = False
            diag1[diag1_index] = False
            diag2[diag2_index] = False
    return False

solve(base_diag1, base_diag2, base_columns, 0)
print(solution_number)
