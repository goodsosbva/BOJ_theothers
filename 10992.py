n = int(input())
m = n
for i in range(1, n + 1):
    if m == i:
        print("*"*(2*i - 1))
    elif i == 1:
        print(" " * (n - i) + "*")
    else:
        print(" " * (n - i) + "*" + " " * int(2*(i-1) - 1) + "*")