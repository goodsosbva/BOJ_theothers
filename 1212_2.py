octnumber = input()

Binum = ''
order = 0


#  while octnumber > 0:
for i in octnumber:

    k = int(i)

    if octnumber == '0':
        Binum += str(0)
        break
    #  print("i값:", k)
    zeroplus = 0
    tmp = ''

    while k > 0:
        tmp = str(k % 2) + tmp
        k = k // 2
        zeroplus += 1
        #print("1:", tmp)

    if order == 0:
        Binum += tmp
        order += 1
    else:
        Binum += ("0" * (3 - zeroplus) + tmp)
    #print("2:", tmp)
print(Binum)


