import sys

n, k = sys.stdin.readline().split(" ")
#n, k = input().split(" ", 1)
#print(n)
#print(k)
N = int(n)
K = int(k) - 1
#numbers = []
#sortedNumbers = []

#for num in range(N):
numbers = list(map(int, input().split()))


numbers.sort()
print(numbers[K])


