n = int(input())
for x in range(n):
    a, b = [int(o) for o in input().split()]
    if max(a, b)/2 > min(a,b):
        print("NO")
    else:
        if (a+b) % 3 == 0:
            print("YES")
        else:
            print("NO")