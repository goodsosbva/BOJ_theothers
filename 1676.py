n = int(input())

res = 1
cnt = 0
flag = True
result = ''

for i in range(1, n + 1):
    res *= i


print(res)
toStr = str(res)
result += toStr
#print(toStr.count("0"))

for i in result[::-1]:

    if i == "0":
        cnt += 1
        #flag = False
    elif i != "0":
        break

print(cnt)
