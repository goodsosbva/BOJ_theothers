from itertools import combinations

lst = []
for _ in range(9):
    lst.append(int(input()))

result = list(combinations(lst, 7))
resultList = [list(comb) for comb in result]
answer = []
for l in resultList:
    if sum(l) == 100:
        answer.extend(l)
        break

for a in answer:
    print(a)