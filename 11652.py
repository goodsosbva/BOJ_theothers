import sys

""""
n = int(sys.stdin.readline())
cards = []
count = 0
number = 1
numberNext = 2
maxCount = 0
maxNumber = 0

for i in range(n):
    k = int(sys.stdin.readline())
    cards.append(k)

cards.sort()

print(cards)

for card in cards:
    if card == number:
        count += 1
    else:
        number += 1
        numberNext += 1
        count += 1

    if maxCount < count and number < numberNext:
        maxCount = count
        maxNumber = card
        number += 1
        count = 0

print(maxNumber)
"""""
import sys

n = int(sys.stdin.readline())
dicCard = {}

for card in range(n):
    tmpCard = int(sys.stdin.readline())
    if tmpCard in dicCard:
        dicCard[tmpCard] += 1
    else:
        dicCard[tmpCard] = 1


print(dicCard)
print(dicCard.items())
dic = sorted(dicCard.items(), key=lambda x: (-x[1], x[0]))
dic_1 = sorted(dicCard.items(), key= lambda x: (x[1]))

print(dic[0][0])
print(dic)
print(dic_1)