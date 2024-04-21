# 첫 번째 줄에서 N을 읽어옴
N = int(input())

# N x N 크기의 이차원 리스트를 입력받음
matrix = [list(map(int, input().split())) for _ in range(N)]

bluePageCount = 0
whitePageCount = 0
def checkBlueConfetti(x, y, n):
    global bluePageCount
    global whitePageCount
    currentColor = matrix[x][y]

    for i in range(x, n):
        for j in range(y, n):
            if currentColor != matrix[i][j]:
                checkBlueConfetti(i, j, n//2)
                checkBlueConfetti(i + n//2, j, n//2)
                checkBlueConfetti(i, j + n//2, n//2)
                checkBlueConfetti(i + n//2, j + n//2, n//2)
                return
    
    if currentColor == 1:
        bluePageCount += 1
    else:
        whitePageCount += 1


# def checkWhiteConfetti(x, y, n):
#     global whitePageCount

#     for i in range(x, n):
#         for j in range(y, n):
#             if matrix[i][j] == 1:
#                 checkWhiteConfetti(i, j, n//2)
#                 checkWhiteConfetti(i + n//2, j, n//2)
#                 checkWhiteConfetti(i, j + n//2, n//2)
#                 checkWhiteConfetti(i + n//2, j + n//2, n//2)
#                 return
#     whitePageCount += 1


checkBlueConfetti(0, 0, N)
print(whitePageCount)
print(bluePageCount)