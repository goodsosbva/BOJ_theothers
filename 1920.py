# 1920.수 찾기
import sys
n = int(sys.stdin.readline())
# n = int(input())
object_list = list(map(int, input().split()))
m = int(sys.stdin.readline())
is_list = list(map(int, input().split()))


for j in range(m):
    if is_list[j] in object_list:
        print(1)
    else:
        print(0)


"""
5
4 1 5 2 3
5
1 3 7 9 5
"""