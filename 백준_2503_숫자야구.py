n = int(input())

def checkStrikeAndBall(pitching):
    isAnswer = True

    for st in steps:
        pitch, strike, ball = st
        
        strPitch = str(pitch)
        s = 0
        b = 0
        for i in range(3):
            if strPitch[i] == pitching[i]:
                s += 1
            elif strPitch[i] in pitching and strPitch[i] != pitching[i]:
                b += 1


        if s != strike or b != ball:
            isAnswer = False
            break
   

    return isAnswer


answer = 0
steps = []
for _ in range(n):
    inputs = list(map(int, input().split()))
    steps.append(inputs)


for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or i == k or j == k:
                continue
            
            pitching = str(i) + str(j) + str(k)
            isAnswer = checkStrikeAndBall(pitching)
            
            if isAnswer:
                answer += 1

print(answer)


