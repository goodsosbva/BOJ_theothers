# 2750. 수 정렬하기
n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))

sorted_nums = sorted(nums, reverse=False)
for n in sorted_nums:
    print(n)
