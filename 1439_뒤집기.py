# 1439. 뒤집기

# 11001100110011000001 -> 4
numbers = [int(num) for num in input()]

count0 = 0
count1 = 0

prev = -1
for i in numbers:
    if i == 0:
        prev = 0
        continue
    elif i == 1 and prev != 1:
        count1 += 1
        prev = 1
    elif i == 1 and prev == 1:
        continue

prev = -1
for i in numbers:
    if i == 1:
        prev = 1
        continue
    elif i == 0 and prev != 0:
        count0 += 1
        prev = 0
    elif i == 0 and prev == 0:
        continue

print(count0, count1)
print(min(count0, count1))
