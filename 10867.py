# 10867. 중복 빼고 정렬 하기

n = int(input())
numbers = list(map(int, input().split()))

new_nums = list(set(numbers))
new_nums.sort()

for i in range(len(new_nums)):
    print(new_nums[i], end=" ")

"""
import sys
input = sys.stdin.readline

n = int(input().rstrip())

visited = [0 for _ in range(2001)] # -1000 ~ 1000 을 0 ~ 2000으로
num_list = list(map(int, input().rstrip().split()))

# set을 대체할 재밌는 방법법
an_list = []
for x in num_list:
    if visited[x+1000] == 0:
        visited[x+1000] = 1
        ans_list.append(x)
        

ans_list.sort()
for x in ans_list:
    print(x, end = " ")
"""
