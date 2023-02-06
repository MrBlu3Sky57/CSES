output = []
q = int(input())
for h in range(q):
    a = input().split()
    x = int(a[1]) 
    y = int(a[0])
    if x > y:
        if x % 2 == 0:
            output.append((x-1)*(x-1) + y)
        else: 
            output.append(x*x - y + 1)
    else:
        if y % 2 != 0:
            output.append((y-1)*(y-1) + x)
        else: 
            output.append(y*y - x + 1)  


_ = [print(o) for o in output]
