def answer(numbers):
    numbers.sort()
    rembersNumbers = set()
    
    for i in range(len(numbers)):
        target = numbers[i]
        if target not in rembersNumbers:
            rembersNumbers.add(target)
            left = i + 1
            right = len(numbers) - 1

            while left <= right:
                mid = (left + right) // 2

                if numbers[mid] > target:
                    right = mid - 1
                elif numbers[mid] < target:
                    left = mid + 1
                else: 
                    if mid != i:
                        return True
                break
        else:
            return True

    return False

numbers = list(map(int, input().split()))

print(answer(numbers))
