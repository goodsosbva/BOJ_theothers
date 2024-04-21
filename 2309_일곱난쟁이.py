dwarfs = []
for i in range(9):
    n = int(input())
    dwarfs.append(n)

l = 0
r = len(dwarfs) - 1
total = sum(dwarfs)
target = 100
dwarfs.sort()
answerList = []
while l < r:
    summary = total - dwarfs[l] - dwarfs[r]

    if summary == target:
        answerList.extend(dwarfs[:l])
        answerList.extend(dwarfs[l + 1: r])
        answerList.extend(dwarfs[r + 1:])
        break

    elif summary > target:
        l += 1
    elif summary < target:
        r -= 1

for a in answerList:
    print(a)

