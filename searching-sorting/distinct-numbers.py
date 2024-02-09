n = int(input())
nums = input().split()

item_set = set()
for x in nums:
    item_set.add(x)

print(len(item_set))