n, k, b = map(int, input().split())

answer = float('inf') 
lamp = [1 for _ in range(n + 1)]
for _ in range(b):
    br = int(input())
    lamp[br] = 0

tmp = 0
for i in range(1, k + 1):
    if lamp[i] == 0:
        tmp += 1
    
l = 1
r = k + 1

# print(lamp)
answer = tmp
while r <= n:
    

    if lamp[r] == 0:
        tmp += 1

    if lamp[l] == 0:
        tmp -= 1

    l += 1
    r += 1

    answer = min(answer, tmp)


print(answer)