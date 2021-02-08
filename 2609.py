a, b = map(int, input().split())

i = 1
j = 1
commonDivisonA = []
commonDivisonB = []
ans = []
ans1 = []
ans2 = []

while i < a:
    commonDivisonA.append(1)
    if a % i == 0:
        commonDivisonA.append(int(a / i))
        i += 1
    else:
        i += 1

while j < b:
    commonDivisonB.append(1)
    if b % j == 0:
        commonDivisonB.append(int(b / j))
        j += 1
    else:
        j += 1

#print(commonDivisonA)
#print(commonDivisonB)

for k in commonDivisonA:
    if k in commonDivisonB:
        ans.append(k)


ans.sort()
#print(ans)
print(ans.pop(-1))

#lowestCommonMultiple = 1
#for q in ans:
#    lowestCommonMultiple *= q

#print(lowestCommonMultiple)
#lowestCommonMultiple = ans.pop()

for k in commonDivisonA:
    if k not in commonDivisonB:
        ans1.append(k)

ans1.sort()
ans1.pop(-1)

for k in commonDivisonB:
    if k not in commonDivisonA:
        ans1.append(k)

ans1.sort()
ans1.pop(-1)

#  ans1.append(lowestCommonMultiple)
#print(ans1)

#  greatestCommonFactor

greatestCommonFactorA = []
greatestCommonFactorB = []


#for w in ans1:
#    greatestCommonFactor *= w

#print(greatestCommonFactor)
k = a

for i in range(1, 1000):
    a = a * i
    greatestCommonFactorA.append(a)

    a = k


greatestCommonFactorA.sort()
#print(greatestCommonFactorA)

l = b

for j in range(1, 1000):
    b = b * j
    greatestCommonFactorB.append(b)

    b = l

greatestCommonFactorB.sort()
#print(greatestCommonFactorB)

for k in greatestCommonFactorA:
    if k in greatestCommonFactorB:
        ans2.append(k)

#print(ans2)
ans2.sort()
print(ans2.pop(0))










