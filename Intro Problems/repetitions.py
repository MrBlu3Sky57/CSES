n = input()
y = n[0]
counter = 0
best = 0

for x in n:
    if x == y:
        counter = counter + 1
    else:
        y = x
        counter = 1
    best = max(best, counter)
print(best)