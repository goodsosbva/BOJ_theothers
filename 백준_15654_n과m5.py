n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers)
sequence = []

def recursion():
    if len(sequence) == m:
        print(*sequence, sep=" ")
        return
    
    for n in sorted_numbers:
        if n not in sequence:
            sequence.append(n)
            recursion()
            sequence.pop()

    
recursion()
