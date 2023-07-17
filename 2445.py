n = int(input())

m = n
if n>=0 and n<101:
    for i in range(1,n+1):
        print("*"*(i) + ' '*(-2*i+2*m) + "*"*(i))

    for j in range(n-1,0,-1):
        print("*"*(j) + ' '*(-2*j+2*m) + "*"*(j))




