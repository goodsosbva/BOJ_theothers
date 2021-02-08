n, k = (input().split())

numbers = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#n = int(n)
k = int(k)
Bnumbers = []
Nnumbers = []
NewNumbers = 0


for i in n:
    Bnumbers.append(i)

for q in Bnumbers:
    idx = 0
    for j in numbers:
        if q == j:
            Nnumbers.append(idx)
        else:
            idx += 1


#print("b:", Bnumbers)
#print(Nnumbers)
evolution = 0
#print(type(evolution))

for i in Nnumbers[::-1]:
    #print(type(i))
    #print(type(k))
    NewNumbers += int(i) * (int(k) ** int(float(evolution)))  # (a**i)
    #print("k:", k)
    #print(NewNumbers)
    evolution = evolution + 1

print(NewNumbers)

#while n > 0:
#    NewNumbers.append(Bnumbers[n % 10])
#    n = n // k


#NewNumbers.reverse()

#for num in NewNumbers:
#    print(num, end="")