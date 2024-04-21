#  n, k = map(int, input().split())
k = 1000000

primeis = [True] * (k + 1)
m = int(k ** 0.5)
    # print(primeis)
primeis[1] = False  # 1 예외처리
primenums = []

for i in range(2, m + 1):
    if primeis[i]:
        for j in range(i + i, k + 1, i):
                # print("j:", j)
            primeis[j] = False
    # print(primeis)
    # print("\n")
    #for q in range(3, k + 1):
    #    if primeis[q]:
    #        primenums.append(q)

#print(primeis)
    #print(primenums)


while True:
    i = int(input())

    if i == 0:
        break

    for j in range(3, k):
        if primeis[j] == True:
            if primeis[i - j] == True:
                print("%d = %d + %d" %(i, j, i - j))
                break


