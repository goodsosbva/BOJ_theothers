import sys

input = sys.stdin.readline


def update(i, diff):  # diff = 1 // for 문에서 호출할때는 -1
    while i < size:
        print("i계산 전:", i)
        bit[i] = bit[i] + diff
        i |= i + 1  # i 와 i + 1 or 연산

        print(bit)
        print("i계산 후:", i)
        print("============")

def get(x): # def get(x + 1) 형태로 호출 , size: 4
    left, right = 0, size
    for i in range(exp + 1):
        mid = (left + right) >> 1
        print("mid:", mid)
        val = bit[mid - 1]

        print("val:", val, end=" <==== ")
        print("bitInGet[mid-1]:", bit)
        print("x:", x)

        if val >= x:
            right = mid
            print("right:", right)
            print("-------------")
        else:
            left = mid
            x -= val
            print("left:", left)
            print("x -= val:", x)
            print("-------------")


    return left


n, k = map(int, input().split())

exp, size = 0, 1

while size < n:
    exp += 1
    size *= 2
bit = [0] * size

print("size:", size)
print("exp:", exp)
print("bit:", bit)
print("=============")

for i in range(n):
    print("update i:", i)
    update(i, 1)

    print("부분 업데이트 종료")
    print("=============")

print("+++++++첫 업데이트 끝!+++++++")

print("size:", size)
print("exp:", exp)
print("bit:", bit)
print("=============")

ans = []
x = 0

for j in range(n, 0, -1):
    x = (x + k - 1) % j

    print("{{{get  시작!!!!}}}")
    val = get(x + 1)
    print("{{{get 끝!!!!}}}")
    print("val:", val)
    print("새로운 업데이트 시작!!!")
    update(val, -1)
    print("[[[[ans.append]]]]")
    print("val + 1:", val + 1)
    ans.append(val + 1)
    print("ans:", ans)

print("\n")
sys.stdout.write(f'<{", ".join(map(str, ans))}>')