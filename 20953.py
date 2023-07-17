import sys


def dolmen(a, b):
    sum = 0
    sum = sum + ((a + b) ** 2 * (a + b - 1)) // 2

    return sum


TestCase = int(sys.stdin.readline())
for q in range(TestCase):
    a, b = map(int, sys.stdin.readline().split())
    res = dolmen(a, b)
    print(res)
