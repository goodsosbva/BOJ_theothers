n, k = map(int, input().split())

res = 1
resM = 1
resMN = 1
cnt = 0
v = n - k

result = ''

for i in range(1, n + 1):
    res *= i

for j in range(1, k + 1):
    resM *= j

for s in range(1, v + 1):
    resMN *= s

final = res // (resM * resMN)
#print(final)
toStr = str(final)
result += toStr
#print(toStr.count("0"))

for i in result[::-1]:

    if i == "0":
        cnt += 1
        #flag = False
    elif i != "0":
        break

print(cnt)