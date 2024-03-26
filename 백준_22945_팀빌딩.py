# n = int(input())

# numbers = list(map(int, input().split()))

# l = 0
# r = len(numbers)
# maxValue = 0

# while l < r:
#     maxValue = max(maxValue, (r - l - 2) * min(numbers[l], numbers[r - 1]))
    
#     if numbers[l] < numbers[r - 1]:
#         l += 1
#     else:
#         r -= 1
  

# print(maxValue)

n = int(input())

numbers = list(map(int, input().split()))

l = 0
r = len(numbers)
maxValue = -1

while l < r:
    
    
    summary = (r - l - 2) * min(numbers[l], numbers[r - 1])
    maxValue = max(maxValue, summary)
    if numbers[l] < numbers[r - 1]:
        l += 1
    else:
        r -= 1


print(maxValue)



