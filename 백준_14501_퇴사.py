n = int(input())

consulting = []
for i in range(n):
    t, p = map(int, input().split())
    consulting.append([t, p])


answer = 0
def recursion(day, profit):
    global answer
    if day == n:
        answer = max(answer, profit)
        return
    

    if day + consulting[day][0] <= n:
        recursion(day + consulting[day][0], profit + consulting[day][1])

    recursion(day + 1, profit)


recursion(0, 0)
print(answer)