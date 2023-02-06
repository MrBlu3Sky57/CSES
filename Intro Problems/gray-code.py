# n = int(input())
# k = 2**n

# list = []

# i = 0
# j = 1

# while k > 1:
#     temp = []
#     while len(temp) < 2**n:
#         temp.extend([i for x in range(k//2)])
#         temp.extend([j for x in range(k//2)])
#         z = i
#         i = j
#         j = z
#     k = k//2
#     list.append(temp)

# for x in range(2**n):
#     for y in range(n):
#         print(list[y][x], end="")
#     print()

n = int(input())
for i in range(2**n):print(bin(i^(i>>1))[2:].zfill(n))

print(8^2)
 

    