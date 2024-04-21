n, k = map(int, input().split())

temp = [0] * 2
print(temp)
A = [i for i in range(1, n + 1)]
print(A)


def comb(n, k):
    print("comb(n, k):", n, k)
    if k == 0:
        print(temp)

    elif n < k:
        return

    else:
        temp[k - 1] = A[n - 1]
        comb(n - 1, k - 1)
        comb(n - 1, k)



comb(n, k)
