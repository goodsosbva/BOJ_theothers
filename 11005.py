n, k = (input().split())

numbers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n = int(n)
k = int(k)
Bnumbers = []

while n > 0:
    Bnumbers.append(numbers[n % k])
    n = n // k


Bnumbers.reverse()

for num in Bnumbers:
    print(num, end="")



