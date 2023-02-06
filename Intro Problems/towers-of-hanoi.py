n = int(input())
print(2**n - 1)

def solve(n, initial, middle, final):
    if n == 1:
        print(initial, " ", final)
    else:
        solve(n-1, initial, final, middle)
        print(initial," ",final )
        solve(n-1, middle, initial, final)   

solve(n, 1, 2, 3)
