'''
9
5 12 7 10 9 1 2 3 11
13
'''
n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()

r = 0
l = len(nums) - 1
ans = 0
while r < l:
    isSame = nums[r] + nums[l]
    if isSame == x:
        r += 1
        l -= 1
        ans += 1

    elif isSame > x:
        l -= 1
    elif isSame < x:
        r += 1

print(ans)