n = int(input())

ropes = []
for _ in range(n):
    rope = int(input())
    ropes.append(rope)

sorted_rope = sorted(ropes)

answer = 0
for i in range(len(sorted_rope)):
    length = len(sorted_rope) - i
    ans = length * sorted_rope[i]
    answer = max(ans, answer)

print(answer)

