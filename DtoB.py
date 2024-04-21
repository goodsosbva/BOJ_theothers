decNum = int(input("이진수로 바꿀 십진수를 입력하시오: "))

binaryArr = []

while (decNum > 0):
    binaryArr.append(decNum % 2)
    print(binaryArr)

    decNum = decNum // 2
    print(decNum)

binaryArr.reverse()

for bDigit in binaryArr:
    print(bDigit, end='')

