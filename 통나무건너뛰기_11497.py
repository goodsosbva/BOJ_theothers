tc = int(input())

for _ in range(tc):
    n = int(input())

    logs = list(map(int, input().split()))
    listLog = list(logs)
    listLog.sort()

    stack1 = []
    stack2 = []
    for i in range(len(listLog)):
        if i % 2 == 0:
            stack1.append(listLog[i])
        else:
            stack2.append(listLog[i])

    stack1.sort(reverse=True)

    candAnserList = stack1 + stack2

    tmp = []
    for i in range(len(candAnserList)):
        if i == len(candAnserList) - 1:
            candi = abs(candAnserList[i] - candAnserList[0])
        else:
            candi = abs(candAnserList[i] - candAnserList[i + 1])

        tmp.append(candi)
    tmpMax = max(tmp)

    print(tmpMax)



"""
1
7
13 10 12 11 10 11 12
"""

