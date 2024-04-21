# 200
# 19

n = int(input())

numbers = []
count = 1
while n != 0:
    n -= count
    if n >= 0:
        numbers.append(count)
        count += 1
    elif n < 0:
        break

print(len(numbers))