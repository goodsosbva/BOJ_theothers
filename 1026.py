# 1026. 보물
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
# print(a, b)
res = 0
for i in range(n):
    res += a[i] * b[i]

print(res)


def quick_sort(lst):  # 퀵정렬
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    less_arr, equal_arr, big_arr = [], [], []
    for i in lst:
        if i < pivot:
            less_arr.append(i)
        elif i > pivot:
            big_arr.append(i)
        else:
            equal_arr.append(i)
    return quick_sort(less_arr) + equal_arr + quick_sort(big_arr)
