n = int(input())

numbers = []
sum = 0

weights = input().split(" ")
for x in range(n):
    num = int(weights[x])
    sum += num
    numbers.append(num)

target = sum / 2
def generate_subsets(current_list, n, current_sum, best_difference):

    if n == len(numbers):
        return abs(current_sum - target)

    best_diff1 = generate_subsets(current_list, n + 1, current_sum, best_difference)
    current_list.append(numbers[n])
    best_diff2 = generate_subsets(current_list, n + 1, current_sum + numbers[n], best_difference)
    current_list.pop()

    return min(best_diff1, best_diff2)

best_difference = generate_subsets([], 0, 0, target)
print(int(best_difference * 2))





    



