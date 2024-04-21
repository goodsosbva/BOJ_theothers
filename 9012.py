n = int(input())

count = 0

for i in range(n):
    #while True:
    b = input()
    s = list(b)
    for k in s:

        if k == '(':
            count += 1

        elif k == ')':
            count -= 1

        if count < 0:
            print("NO")
            break



    if count == 0:
        print("YES")
    elif count > 0:
        print("NO")
    #print("count", count)
    count = 0
