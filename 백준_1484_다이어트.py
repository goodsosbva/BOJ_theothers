g = int(input())

answerList = []
curWeight = 1
oldWeight = 1
while True:
    if curWeight * curWeight - oldWeight * oldWeight == g:
        answerList.append(curWeight)
        curWeight += 1

    elif curWeight * curWeight - oldWeight * oldWeight < g:
        curWeight += 1
    
    elif curWeight - oldWeight != 1 and curWeight * curWeight - oldWeight * oldWeight > g:
        oldWeight += 1

    # 탈출 조건 g 보다 큰데 현재 값이 가장 작은 값인 상황 그럼 더 볼 필요 없는 것
    if curWeight - oldWeight == 1 and curWeight * curWeight - oldWeight * oldWeight > g:
        break


if len(answerList) == 0:
    print(-1)
else:
    for a in answerList:
        print(a)