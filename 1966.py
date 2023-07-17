# 1966. 프린터 큐
from collections import deque

testcase = int(input())
for ts in range(testcase):
    n, m = map(int, input().split())
    priority_nums = deque(list(map(int, input().split())))
    # print(list(priority_nums))
    # q = deque(priority_nums)
    # print(priority_nums)
    idx = deque(list(range(n)))
    cnt = 0
    while priority_nums:
        # top_prior = max(priority_nums)
        if max(priority_nums) == priority_nums[0]:
            cnt += 1
            priority_nums.popleft()
            if idx.popleft() == m:
                print(cnt)

        else:
            priority_nums.append(priority_nums.popleft())
            idx.append(idx.popleft())


"""
1
4 2
1 2 3 4
"""

