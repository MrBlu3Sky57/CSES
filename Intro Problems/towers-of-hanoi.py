n = int(input())
print(2**n - 1)


def solve(start, aux, end, k):
    if k > n:
        return
    solve(start, end, aux, k + 1)
    print(f"{start} {end}")
    solve(aux, start, end, k + 1)

solve(1, 2, 3, 1)