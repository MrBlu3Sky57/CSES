import math

alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_bank = {}

for x in range(len(alphabet)):
    letter_bank[alphabet[x]] = x + 1

input = input()
string = list(input)

n = len(string)

chars = {}
for x in string:
    if x in chars:
        chars[x] += 1
    else:
        chars[x] = 1

divisor = 1
for key, value in chars.items():
    divisor = divisor * math.factorial(value)

total = math.factorial(n) / divisor
print(int(total))


for x in range(n - 1):
    for y in range(n - 1):
        if letter_bank[string[y]] > letter_bank[string[y + 1]]:
            z = string[y]
            string[y] = string[y + 1]
            string[y + 1] = z

chosen = [False] * n
permutation = []
set = set()
def search():
    if len(permutation) == n:
        output = ''.join(permutation)
        if output not in set:
            set.add(output)
            print(output)
            return
    else:
        for x in range(n):
            if chosen[x] == True: continue
            chosen[x] = True
            permutation.append(string[x])
            search()
            permutation.reverse()
            permutation.remove(string[x])
            permutation.reverse()
            chosen[x] = False
search()
