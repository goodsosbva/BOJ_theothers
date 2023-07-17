x = int(input())
numbers = []

#for i in range(x):
#    y = int(input())
#    numbers.append(y)
numbers = list(map(int,input().split()))
max = numbers[0]
min = numbers[0]

for j in numbers:
    if max < j:
        max = j

for k in numbers:
    if min > k:
        min = k

print(min,max)
