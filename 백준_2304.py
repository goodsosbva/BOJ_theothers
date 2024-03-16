n = int(input())

coordi = []
maxHeight = -1
maxIdx = -1
answer = 0

for i in range(n):
    x, y = map(int, input().split())

    coordi.append([x, y])

coordi.sort()

for i in range(len(coordi)):
    x, y = coordi[i]

    if y > maxHeight:
        maxHeight = y
        maxIdx = i


height = coordi[0][1]
for i in range(maxIdx):
    x1, y1 = coordi[i]
    x2, y2 = coordi[i + 1]

    if height < y2:
        base = x2 - x1

        answer += base * height
        height = y2
    
    elif height >= y2:
        base = x2 - x1
        answer += height * base



height = coordi[-1][1]
for i in range(len(coordi) - 1, maxIdx, -1):
    x1, y1 = coordi[i]
    x2, y2 = coordi[i - 1]

    if height < y2:
        base = x1 - x2 

        answer += base * height

        height = y2
    
    elif height >= y2:
        base = x1 - x2 
        answer += height * base

print(answer + maxHeight)


'''
3
0 3
1 2
2 3
답 9


4
1 3
2 2
3 3
4 3
답 12


5
4 3
6 5
9 5
11 3
13 4
답 42
'''