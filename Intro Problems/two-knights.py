n = int(input())
for x in range(1, n+1):
    if x > 2:
        print(int((x*x)*(x*x-1)/2-(x-2)*(x*4-4)))
    elif x == 1:
        print(0)
    else:
        print(6)