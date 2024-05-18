n, m = map(int, input().split())
numbers = list(map(int, input().split()))
sortedNumbers = sorted(numbers)
sequence = []
answerList = []

def recurison():
    if len(sequence) == m:
        sortedSequence = sorted(sequence)
        if sortedSequence not in answerList:
            print(*sortedSequence, sep=' ')
            answerList.append(sortedSequence)
        return
    
    for n in sortedNumbers:
        if n not in sequence:
            sequence.append(n)
            recurison()
            sequence.pop()

recurison()