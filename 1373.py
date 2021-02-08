n = input()

Bnumbers = []
NewNumbers = 0
evolution = 0
#result = ''

for j in n:
    Bnumbers.append(int(j))

#print(Bnumbers)

for i in Bnumbers[::-1]:
    w = int(i)
    NewNumbers += w * (2 ** int(evolution))  # (a**i)
    evolution = evolution + 1

#print(NewNumbers)
octetArr = ''

while NewNumbers > 0:
    octetArr += str(NewNumbers % 8)
    #print(octetArr)
    NewNumbers = NewNumbers // 8

print(octetArr[::-1])
