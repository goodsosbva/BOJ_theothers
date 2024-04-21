N, K = input().split()

n = int(N)
k = int(K) - 1
num = k

circular = []
humans = []

circular = [i for i in range(1, n + 1)]
#for i in range(1, n + 1):
#    circular.append(i)


for i in range(n):
    #num += k
    if num < len(circular):
    #    #print("if")
        humans.append(str(circular.pop(num)))
        num += k
    elif num >= len(circular):
        # print("elif")
        num = num % len(circular)
        humans.append(str(circular.pop(num)))
        num += k

    #humans.append(str(circular.pop(num)))

# print(humans)
print("<", ", ".join(humans)[:], ">", sep="")
