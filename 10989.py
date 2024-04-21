import sys

n = int(sys.stdin.readline())

arraySort = [0] * 10001

#for i in range(n):
#    k = int(sys.stdin.readline())
#    arraySort.append(k)

for i in range(n):
    arraySort[int(sys.stdin.readline())] += 1

#arraySort.sort()
print('arrraySort[2]: %s\n' % 2 * arraySort[2], end="")
#for i in arraySort:
#    print(i)
for i in range(10001):
    if arraySort[i] != 0:
        for _ in range(arraySort[i]):
            print(i)
        #print('%s\n' % i * arraySort[i], end="")