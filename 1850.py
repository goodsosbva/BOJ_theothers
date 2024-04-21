a, b = map(int, input().split())

def greatestCommonFactor(a, b):

    if b == 0:
        return a

    return greatestCommonFactor(b, a % b)



def lowestCommonMultiple(a, b, gcd):
    a = a / gcd
    b = b / gcd
    lcm = a * b * gcd

    return lcm

gcd = greatestCommonFactor(a, b)
#print(gcd)

for i in range(gcd):
    print("1", end="")

#lcm = lowestCommonMultiple(a, b, gcd)
#print(int(lcm))
