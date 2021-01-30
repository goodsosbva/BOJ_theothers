# 재귀를 이용한 정렬
def mergeSort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    print("시작 array: ", array)
    print("mid: ", array[mid])
    left = mergeSort(array[:mid])
    print("left: ", left)
    right = mergeSort(array[mid:])
    print("right: ", right)

    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        print(array)
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
            print("if:", array)
        else:
            array[k] = right[j]
            j += 1
            print("else:", array)
        k += 1
        print("i, j, k: ",i, j, k)

    if i == len(left):
        while j < len(right):
            array[k] = right[j]
            print("if_while:", array)
            j += 1
            k += 1
            print("i, j, k: ", i, j, k)
    elif j == len(right):
        while i < len(left):
            array[k] = left[i]
            print("elif_while:", array)
            i += 1
            k += 1
            print("i, j, k: ", i, j, k)
    return array


n, k = map(int, input().split())

num = list(map(int, input().split()))
num = mergeSort(num)

print(num)
