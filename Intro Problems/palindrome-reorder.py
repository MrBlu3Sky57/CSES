from collections import Counter

n = input()
k = int((len(n) - 1)/2)
dict = {'A': 0}
oddCounter = 0
oddKey = 0
list = [0] * len(n)

i = 1
for x in n:
    if x in dict:
        i = dict[x] + 1
    dict[x] = i
    i = 1
if (len(dict) * 2) - 1 > len(n):
    print("NO SOLUTION")
else:
    for x in dict:
        if dict[x] % 2 == 1:
            oddKey = x
            oddLength = dict[x]
            oddCounter = oddCounter + 1
            if oddCounter > 1:
                print("NO SOLUTION")
                break
    g = 0
    h = len(n) - 1
    if oddKey != 0:
        if oddLength == 1:
            list[k] = oddKey
        else:
            for x in range(oddLength-1):
                list[k] = oddKey
                list[k - x] = oddKey
                list[k + x] = oddKey

        for x in dict:
            if x != oddKey:
                for o in range(int(dict[x]/2)):
                    list[g] = x
                    g = g + 1
                    list[h] = x
                    h = h - 1
                    if g == k or h == k:
                        break
    else:
        for x in dict:
            for o in range(int(dict[x]/2)):
                list[g] = x
                g = g + 1
                list[h] = x
                h = h - 1
                if h == k:
                    break
    _ = [print(o, end="") for o in list]
