n = int(input())

m = n
if n>=0 and n<101:
    for i in range(0,n):
        print(" "*(i) + '*'*(-2*i+2*m-1))

    for j in range(n-2,-1,-1):
        print(" "*(j) + '*'*(-2*j+2*m-1))


