from collections import deque
t = int(input())
for _ in range(t):
    n, x = map(int,input().split())
    priority_nums = deque(list(map(int, input().split())))
    idx_que = deque(list(range(n)))
    cnt = 0
    while priority_nums:
        if priority_nums[0] == max(priority_nums):
            cnt += 1
            priority_nums.popleft()
            if idx_que.popleft() == x:
                print(cnt)
        else:
            priority_nums.append(priority_nums.popleft())
            idx_que.append(idx_que.popleft())