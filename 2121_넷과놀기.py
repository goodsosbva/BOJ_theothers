
# def binary_search(t):
#     l = 0
#     r = n - 1
#     while l <= r:
#         m = (l + r) // 2
#         if sDots[m] == t:
#             return True
#         elif sDots[m] > t:
#             r = m - 1
#         else:
#             l = m + 1
#     return False
#
#
# n = int(input())
# garo, sero = map(int,input().split())
#
# dots = []
# for _ in range(n):
#     x, y = map(int, input().split())
#     dots.append((x, y))
#
# sDots = sorted(dots, key=lambda x : (x[0], x[1]))
# answer = 0
# for dot in sDots:
#     x, y = dot
#
#     if binary_search((x + garo, y)) and binary_search((x, y + sero)) and binary_search((x + garo, y + sero)):
#         answer += 1
#
# print(answer)

n = int(input())
garo, sero = map(int, input().split())

dots = set()
for _ in range(n):
    x, y = map(int, input().split())
    dots.add((x, y))

answer = 0
for dot in dots:
    x, y = dot

    if (x, y + sero) in dots and (x + garo, y) in dots and (x + garo, y + sero) in dots:
        answer += 1

print(answer)