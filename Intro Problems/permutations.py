n = int(input())
oddStr = ""
evenStr = ""
if 1 < n < 4:
    print("NO SOLUTION")
else:
    for x in range(1, n+1):
        if x % 2 == 0:
            evenStr = evenStr + str(x) + " "
        else:
             oddStr = oddStr + str(x) + " "
    print(evenStr + oddStr) 