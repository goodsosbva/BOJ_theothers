n = int(input())
if n>=0 and n<101:
    for i in range(n):
        for j in range(n-1,-1,-1):
            if i < j:
                print(" ",end="")
            else:
                print("*", end="")
        for j in range(i):
            print("*",end="")

        print("")