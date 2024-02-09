n, m = map(int, input().split())
tickets = list(map(int, input().split()))
customers = list(map(int, input().split()))

tickets.sort(reverse=True)
pairs = [] * len(customers)

for i in range(0, len(customers)):
    pairs[i] = -1

customers.sort(reverse=True)

i = 0
for c in customers:
    if c >= tickets[-1]:
        if i < len(tickets):
            while tickets[i] > c:
                if i < len(tickets) - 1:
                    i += 1
                else:
                    break
            pairs[c] = tickets[i]
            tickets.pop(i)

_ = [print(e) for e in pairs]
