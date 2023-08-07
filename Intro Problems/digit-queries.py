n = int(input())

queries = []
for x in range(0, n):
    queries.append(int(input()))

def solve(num, n):

    difference = num - (9 * n * 10**(n-1))
    if difference < 1:
        position = num % n
        value = (num + n - 1) // n + (10**(n-1) - 1)

        if position != 0:
            digit = (value // 10 ** (n - position)) % 10
        else:
            digit = value % 10
        return digit 
    else:
        return solve(difference, n+1)
        

for x in queries:
    print(solve(x, 1))