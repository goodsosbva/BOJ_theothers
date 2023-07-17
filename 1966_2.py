# 1966. 프린터 큐2
from collections import deque

test_cases = int(input())

for ts in range(test_cases):
    n, m = list(map(int, input().split()))
    priority = deque(list(map(int, input().split())))
    idx = list(range(n))
    idx[m] = 1004

    # 순서
    order = 0

    while True:
        # imp의 첫번째 값 = 최댓값?
        if priority[0] == max(priority):
            order += 1

            # idx의 첫 번째 값 = 1004?
            if idx[0] == 1004:
                print(order)
                break
            else:
                priority.popleft()
                idx.pop(0)

        else:
            priority.append(priority.popleft())
            idx.append(idx.pop(0))
