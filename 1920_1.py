# 1920_1. 수 찾기
import sys
n = int(sys.stdin.readline())
# n = int(input())
# object_list = list(map(int, input().split()))
# object_list1 = sorted(object_list)
object_list1 = sorted(map(int, input().split()))
m = int(sys.stdin.readline())
is_list = list(map(int, input().split()))


def binary_search(target, object_list1, start, end):
    if start > end:
        # print("0")
        return 0
    mid = (start + end) // 2

    if object_list1[mid] > target:
        return binary_search(target, object_list1, start, mid - 1)
    elif object_list1[mid] < target:
        return binary_search(target, object_list1, mid + 1, end)
    else:
        # print("1")
        return 1


for t in is_list:
    res = binary_search(t, object_list1, 0, n - 1)
    print(res)