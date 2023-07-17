n = int(input())
if n>=0 and n<101:
    for i in range(n-1,-1,-1):
        for j in range(i+1):
            print("*",end="")
        print("")