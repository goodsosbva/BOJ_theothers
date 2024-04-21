import sys

N = int(input())
Sort = []

for i in range(N):
    #n = int(input())
    Sort.append(int(sys.stdin.readline()))

#Sort.sort()
#Sort.reverse()

for i in sorted(Sort):
    sys.stdout.write(str(i) + '\n')