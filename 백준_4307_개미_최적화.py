from itertools import product

tc = int(input())

for _ in range(tc):
    stick, antLength = map(int, input().split())

    startAnt = []
    minAllFallTick = 10000
    maxAllFallTick = 0
    for i in range(antLength):
            startAnt.append([int(input())])

    minFallTick = -1
    maxFallTick = 10000

    for path in range(len(startAnt)):
        index = 0
        fallTick = -1
        for p in path:
            if p == "R":
                thisFallTick = (stick - 1) - startAnt[index][0]
            else: 
                thisFallTick = startAnt[index][0]

            fallTick = max(thisFallTick, fallTick)
            index += 1

        # print(fallTick)
        minAllFallTick = min(minAllFallTick, fallTick)
        maxAllFallTick = max(maxAllFallTick, fallTick)

    print(minAllFallTick + 1, maxAllFallTick + 1)


 
