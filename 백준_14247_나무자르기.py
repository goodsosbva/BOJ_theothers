# n = int(input())
# initial_heights = list(map(int, input().split()))
# growth_rates = list(map(int, input().split()))

# answer = 0
# for idx in range(n):
#     for jdx in range(n):
#         initial_heights[jdx] += growth_rates[jdx]

#     answer += max(initial_heights)
#     max_idx = initial_heights.index(max(initial_heights))
#     initial_heights[max_idx] = 0

# print(answer)

n = int(input())
initial_heights = list(map(int, input().split()))
growth_rates = list(map(int, input().split()))

trees = list(zip(initial_heights, growth_rates))

trees.sort(key=lambda x: x[1])

answer = 0
for day in range(n):
    answer += trees[day][0] + trees[day][1] * day

print(answer)



