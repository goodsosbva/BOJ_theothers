case = int(input())

def gcd(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x

for i in range(case):
    total = 0
    num = list(map(int,input().split()))
    for i in range(1,len(num)-1):
        for j in range(i+1,len(num)):
            print("1:", num[i])
            print("2:", num[j])
            total += gcd(num[i],num[j])
    print(total)
