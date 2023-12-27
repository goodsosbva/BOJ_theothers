from itertools import product
import copy

# 왼쪽과 오른쪽의 선택지
choices = ['L', 'R']

tc = int(input())

for _ in range(tc):
    stick, antLength = map(int, input().split())

    allPaths = list(product(choices, repeat=antLength))

    startAnt = []
    minAllFallTick = 10000
    maxAllFallTick = 0
    for i in range(antLength):
            startAnt.append([int(input())])

    for tick in range(len(allPaths)):
        tmpStartAnt = copy.deepcopy(startAnt)
        for idx in range(antLength):
            tmpStartAnt[idx].append(allPaths[tick][idx])

        print("tmpStartAnt >> ", tmpStartAnt)
       
        fallTick = 1

        while True:
            isAllOuted = True
            for k in range(len(tmpStartAnt)):
                if tmpStartAnt[k][1] == "R" or tmpStartAnt[k][1] == "L":
                    isAllOuted = False
                    break

            print("fallTick, isAllOuted >>> ", fallTick, isAllOuted)
            if isAllOuted: 
                minAllFallTick = min(minAllFallTick, fallTick)
                maxAllFallTick = max(maxAllFallTick, fallTick)
                break

            for index in range(len(tmpStartAnt)):
                print("curPostion, dirc >>> ", tmpStartAnt[index][0], tmpStartAnt[index][1])
                if tmpStartAnt[index][1] == "R":
                     tmpStartAnt[index][0] += 1

                     if tmpStartAnt[index][0] >= stick - 1:
                          tmpStartAnt[index][1] = "Outed"
                else:
                     tmpStartAnt[index][0] -= 1

                     if tmpStartAnt[index][0] == 0:
                          tmpStartAnt[index][1] = "Outed"

            # for i in range(len(tmpStartAnt)):
            #      for j in range(len(tmpStartAnt)):
            #           if i == j:
            #                continue
                      
            #           if tmpStartAnt[i][0] == tmpStartAnt[j][0] and tmpStartAnt[i][1] != "Outed":
            #                tmpStartAnt[i][0] -= 1
            #                tmpStartAnt[j][0] += 1

            #                tmpStartAnt[i][1] = "L"
            #                tmpStartAnt[j][1] = "R"
            #                print("hello")

            fallTick += 1

        print(minAllFallTick, maxAllFallTick)


'''
1
10 3
2
6
7
'''
 
