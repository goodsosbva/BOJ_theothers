import sys
from collections import deque


N, K = map(int, sys.stdin.readline().split())
circular = deque([i for i in range(1, N + 1)])  # 맨 처음에 원에 앉아있는 사람들

answer = []  # 제거된 사람들을 넣을 배열


while circular:
    circular.rotate(-K + 1)
    answer.append(str(circular.popleft()))

sys.stdout.write("<" + ", ".join(answer) + ">")
#print(answer)

