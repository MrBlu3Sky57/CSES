n, m, k = map(int, input().split())
applicants = list(map(int, input().split()))
apartments = list(map(int, input().split()))

applicants.sort()
apartments.sort()

i = 0
j = 0

num_apt = 0
while i < n and j < m:
    apartment = apartments[j]
    applicant = applicants[i]

    if applicant - k > apartment:
        j += 1
    elif applicant + k < apartment:
        i += 1 
    else:
        i += 1
        j += 1
        num_apt += 1
print(num_apt)