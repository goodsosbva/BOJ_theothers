n = int(input())
twoDimension = []
for i in range(n):
    a, b = input().split()    # 입력받은 값을 공백을 기준으로 분리
    a = int(a)
    b = int(b)
    twoDimension.append([a, b])

# print(twoDimension)
# print(type(twoDimension[0][1]))

twoDimension.sort(key=lambda x: (x[1], x[0]))  # 중요 부분

for i in twoDimension:
    print(i[0], i[1])  # 이런식으로 프린트 할 수 도있다. 알아둘것.