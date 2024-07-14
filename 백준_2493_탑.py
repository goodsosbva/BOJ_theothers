n = int(input())

tops = list(map(int, input().split()))
answer = [0] * n
stack = []

for i in range(n):
    while stack and tops[stack[-1]] < tops[i]:
        stack.pop()

    if stack:
        answer[i] = stack[-1] + 1

    stack.append(i)

for j in range(n):
    print(answer[j], end=' ')