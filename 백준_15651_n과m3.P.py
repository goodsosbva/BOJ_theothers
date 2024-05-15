n, m = map(int, input().split())
sequence = []

def recursion():
    if len(sequence) == m:
        for i in range(len(sequence)):
            if i == len(sequence) - 1:
                print(sequence[i])
            else:
                print(sequence[i], end=' ')
        return


    for i in range(1, n + 1):
        sequence.append(i)
        recursion()
        sequence.pop()

recursion()