A, B, C = input().split()

a = int(A)
b = int(B)
c = int(C)

print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)