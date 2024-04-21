import sys

N = int(input())
sam1 = []
sam2 = []

for i in range(N):
    n = int(sys.stdin.readline())
    if i % 2 == 0:  # i가 짝수인 경우
        sam1.append(n)
    else:
        sam2.append(n)

sam1.sort(reverse=True)
sam2.sort(reverse=True)

try:  # 순차적으로 출력하기위해서 sam1과 sam2의 크기를 비교
    for i in range(N):
        if sam1[-1] < sam2[-1]:
            print(sam1.pop())
        else:
            print(sam2.pop())

except: # 샘플이 먼저 동날 경우 예외 처리
    if len(sam1) == 0:
        for i in range(len(sam2)):
            print(sam2.pop())
    else:
        for i in range(len(sam1)):
            print(sam1.pop())
