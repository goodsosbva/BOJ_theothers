def max_adjacent_difference(arr):
    if len(arr) < 2:
        return None  # 배열의 길이가 2 미만인 경우 비교할 요소가 없음
    
    max_difference = float('-inf')  # 음수 무한대로 초기화

    for i in range(len(arr) - 1):
        difference = abs(arr[i + 1] - arr[i])
        max_difference = max(max_difference, difference)

    return max_difference

# 주어진 배열에 대한 테스트
arr = [1, 3, 5, 12, 5, 6]
result = max_adjacent_difference(arr)
print("인접한 두 요소의 최대 차이:", result)
