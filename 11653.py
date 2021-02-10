n = int(input())

res = []
divednum = 2


while n > 1:

    if n % divednum == 0:
        #print(n)
        n //= divednum
        res.append(divednum)
        divednum = 2

    else:
        #print(n)
        divednum += 1

#print(res)

for i in res:
    print(i)