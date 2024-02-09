n, x = map(int, input().split())
weights = list(map(int, input().split()))
weights.sort()
 
total = 0
light = 0
heavy = len(weights) - 1 

i = 0
while light <= heavy:
    if weights[light] + weights[heavy] <= x:
        light += 1
        heavy -= 1
    else:
        heavy -= 1
    total += 1
       
print(total)