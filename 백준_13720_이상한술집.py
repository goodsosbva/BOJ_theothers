n, k = map(int, input().split())

kettle = []
for _ in range(n):
    makgeolli = int(input())
    kettle.append(makgeolli)


answer = 0
start = 1
end = max(kettle)
count = 0
while True:
    if start > end:
        break

    mid = (start + end) // 2
    cnt = 0

    for i in range(n):
        cnt += kettle[i] // mid

    if cnt == k:
        answer = max(mid, answer)
        start = mid + 1

    elif cnt > k:
        answer = max(mid, answer)
        start = mid + 1
    
    elif cnt < k:
        end = mid - 1


print(answer)
