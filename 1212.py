"""
octnumber = input()
octnumber = octnumber[::-1]
Binum = []
print(octnumber)
#  while octnumber > 0:
for i in octnumber:
    num = 0
    k = int(i)
    print("i값:", k)
    if k < 4 and k > 2:
        Binum.append(0)
    elif k < 2 and k >= 0:
        Binum.append(0)
        Binum.append(0)
    while k > 0:

        Binum.append(k % 2)
        k = k // 2

Binum.reverse()

for n in Binum:
    print(n, end="")


print(Binum)

oc = list(map(int, input()))

bi = ''
for idx, n in enumerate(oc):
    if not idx and not n:
        bi = 0
        break
    temp = ''
    c = 0
    while n:
        temp = str(n % 2) + temp
        n //= 2
        c += 1
    if not idx:
        bi += temp
    else:
        bi += ('0'*(3-c) + temp)
print(bi)

"""

octnum = list(map(int, input()))

binum = ''
#for idx, n in enumerate(octnum):
#    print("(", idx, ",", n, ")", end=" ")
#print("\n")

for idx, n in enumerate(octnum):
    if not idx and not n:
        binum = 0
        break
    tmp = ''
    c = 0
    while n > 0:
        tmp = str(n % 2) + tmp
        #  print("while:" ,tmp)
        n //= 2
        c += 1
    #  print("1:", tmp)
    if not idx:
        binum += tmp
    else:
        binum += ('0' * (3 - c) + tmp)

    #  print("2:", binum)

print(binum)
