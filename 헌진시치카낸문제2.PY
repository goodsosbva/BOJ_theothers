import heapq

def answer(n):
    numbers = [4, 13]
    seen = set(numbers)

    cnt = 0
    while numbers:
        cur = heapq.heappop(numbers)
        cnt += 1

        if cnt == n:
            return cur
        
        for num in [4, 13]:
            next_number = int(str(cur) + str(num))

            if next_number not in seen:
                heapq.heappush(numbers, next_number)
                seen.add(next_number)


n = int(input())
print(answer(n))