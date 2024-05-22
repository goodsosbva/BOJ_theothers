n = int(input())

dasom = 0
candidates = []
for i in range(n):
    if i == 0:
        dasom = int(input())

    else:
        candi = int(input())
        candidates.append(candi)        

answer = 0
while candidates and dasom <= max(candidates):
    max_index = candidates.index(max(candidates))
    if dasom <= candidates[max_index]:
        dasom += 1
        candidates[max_index] -= 1
        answer += 1

print(answer)

