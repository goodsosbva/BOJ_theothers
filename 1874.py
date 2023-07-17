n = int(input())

# numbers = list(map(int, input().split()))
stack_n = []
cnt = 1  # n 만큼 오름차순 수열 역할
# num = 1
# idx = 0
res = []
flag = 0
for i in range(n):
    number = int(input())
    while cnt <= number:
        if cnt <= number:
            stack_n.append(cnt)
            res.append("+")
            cnt += 1
    if stack_n[-1] == number:
        stack_n.pop()
        res.append("-")
    else:  # stack_n[-1] > number
        flag = 1

if flag == 1:
    print("NO")
else:
    for i in res:
        print(i)




