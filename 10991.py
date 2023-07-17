

n = int(input())
m = n + 1
if n>=0 and n<101:
    for i in range(1,m):
        print(" " * (n - i), end="")
        # while m <= (2*i - 1):
        for j in range(1,2*i):

            if j % 2 == 1:
                print("*", end="")
            else:
                print(" ", end="")

        print("")

'''
n = int(input())

m = n
if n>=0 and n<101:
    for i in range(1,n+1):
        print(" " * (n - i) + "* " * i)
'''

