a, b, d = map(int, input().split())

is_sosu = [i for i in range(b + 1)]
is_sosu[0] = is_sosu[1] = 0
for i in range(2, int(b ** 0.5) + 1):
    if is_sosu[i] == 0:
        continue
    for j in range(i * i, b + 1, i):
        is_sosu[j] = 0

answer = 0
for k in range(a, b + 1):
    if is_sosu[k] != 0:
        count = str(is_sosu[k]).count(str(d))
        if count > 0:
            answer += 1

print(answer)
