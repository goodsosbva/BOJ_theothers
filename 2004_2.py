N, M = map(int, input().split())

# 진짜 팩토리얼로 구해서 문제를 해결하게 되면 시간초과 발생 -> 조합을 구한는 가볍게 만드는걸 생각 중....
# 끝자리가 0이라는 것은 10의 배수
# 10은 2와 5로 구성되어 있음
# 조합 공식이 n! / (n - m)! * m! 이므로 17,18줄에서 n // 5 - (n - m) //5 - m // 5 형식으로 빼주는것, 즉 중복 되는 2 와 5의 배수를 빼는 것임
# 2와 5 짝이 맞아야 10이 되므로 2의 개수와 5의 개수중 더 작은게 10의 개수이다.

def countNumber(n, k):
    count = 0
    while n:
        n //= k
        print("n:", n, end= " ")
        count += n
    print("\n")
    return count


fiveCount = countNumber(N, 5) - countNumber(M, 5) - countNumber(N - M, 5)
twoCount = countNumber(N, 2) - countNumber(M, 2) - countNumber(N - M, 2)

ans = min(fiveCount, twoCount)
print(ans)