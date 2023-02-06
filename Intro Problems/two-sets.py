n = int(input())
list1 = []
list2 = []
sum = n*(n+1)/2
setsum = sum/2

if sum % 2 == 0:
    print("YES")
    if n == 3:
        print(1)
        print(3)
        print(2)
        print("2 1")
    else:
        for x in range(n, 0, -1):
            if n % 2 == 0:
                if x <= n/4 or x > n - n/4:
                    list1.append(x)
                else: 
                    list2.append(x)
            else:
                if sum - x > setsum:
                    sum = sum - x
                    list1.append(x)
                elif sum == n:
                    if x != m:
                        list2.append(x)
                else:
                    m = int(sum - setsum)
                    list1.append(m)
                    list2.append(x)
                    sum = n
        print(len(list1))
        _ = [print(o, end=" ") for o in list1]
        print()
        print(len(list2))
        _ = [print(o, end=" ") for o in list2]

else:
    print("NO")
