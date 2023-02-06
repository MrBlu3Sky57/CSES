import math

n = (int(input()))
total = 0
x = int(math.log(n, 5))

for x in range(1, x + 1):
    total = total + int(n/(5**x))
     

print(total)