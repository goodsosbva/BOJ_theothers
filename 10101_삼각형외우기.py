# 10101. 삼각형 외우기

list = []

for i in range(3):
    list.append(int(input()))


def solution(list):
    if sum(list) != 180:
        print('Error')
        return

    list.sort()
    prev = list[0]
    sameCnt = 0
    for i in range(1, len(list)):
        if prev == list[i]:
            sameCnt += 1
        else:
            prev = list[i]

    if sameCnt == 2:
        print('Equilateral')
        return
    elif sameCnt == 1:
        print('Isosceles')
        return
    else:
        print('Scalene')
        return

solution(list)


