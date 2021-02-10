def combinations(arr, r):
    global cnt
    cnt += 1
    print(cnt, "번째")
    for i in range(len(arr)):  # 함수에서 지금할 일
        print("i:", i)
        if r == 1:  # 종료조건
            print("arr[i]:", arr[i])
            yield [arr[i]]
        else:
            for next in combinations(arr[i + 1:], r - 1):  # 다음에 할 일
                print("next: ", next)
                yield [arr[i]] + next


# 아래는 함수를 실행하기 위한 사용법입니다.
global cnt
cnt = 0
for combi in combinations([1, 2, 3], 2):
    print("combi:", combi)