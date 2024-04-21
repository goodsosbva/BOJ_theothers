from itertools import permutations

n, m = map(int, input().split())

numbers = list(range(1, n + 1))

def check_permutation(arr):
    for i in range(len(arr)):
        if i == len(arr) - 1:
            break

        if arr[i] < arr[i + 1]:
            continue
        else:
            return False
    return True

answer = []
for comb in permutations(numbers, m):
    list_comb = list(comb)

    sorted_comb = sorted(list_comb)
    if check_permutation(sorted_comb):
        answer.append(list_comb)

for ans in answer:
    for element in ans:
        print(element, end=' ')
    print()


# 4 2

# 1 2
# 1 3
# 1 4
# 2 1
# 2 3
# 2 4
# 3 1
# 3 2
# 3 4
# 4 1
# 4 2
# 4 3