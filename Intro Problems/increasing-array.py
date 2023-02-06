n = input()
m = input()
m = m.split(' ')
moves = 0
m = [int(num, base = 10) for num in m]
y = m[0]
for x in m:
    if x < y:
        z = y-x
        y = x + z
        moves = z + moves
    else:
        y = x
print(moves)
