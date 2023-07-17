n = int(input())

m = n
if n>=0 and n<101:
    for i in range(1,n+1):
        print(" "*(n-i) + "*"*(i))

    for i in range(n-1,0,-1):
        print(" "*(n-i) + "*"*(i))