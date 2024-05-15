n, m = map(int, input().split())
sequence = []


def recursion(st):
    if len(sequence) == m:
        sorted_sequence = sorted(sequence)
        print(*sorted_sequence, sep=' ')
        return
    
    for i in range(st, n + 1):
        if i not in sequence:
            sequence.append(i)
            recursion(i)
            sequence.pop()


recursion(1)