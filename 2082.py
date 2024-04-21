numbers = [
    ["###", "#.#", "#.#", "#.#", "###"],  # 0
    ["..#", "..#", "..#", "..#", "..#"],  # 1
    ["###", "..#", "###", "#..", "###"],  # 2
    ["###", "..#", "###", "..#", "###"],  # 3
    ["#.#", "#.#", "###", "..#", "..#"],  # 4
    ["###", "#..", "###", "..#", "###"],  # 5
    ["###", "#..", "###", "#.#", "###"],  # 6
    ["###", "..#", "..#", "..#", "..#"],  # 7
    ["###", "#.#", "###", "#.#", "###"],  # 8
    ["###", "#.#", "###", "..#", "###"]  # 9
]

pattern = [input() for _ in range(5)]

# 각 숫자를 분리하여 저장할 배열 초기화
numbersInput = [[] for _ in range(4)]
answer = []

# 입력받은 패턴을 숫자별로 분리
for line in pattern:
    parts = line.split(" ")
    for i, part in enumerate(parts):
        numbersInput[i].append(part)

def chkNumber(inputNumber, number):
    for i in range(3):
        if inputNumber[i] == number[i]:
            continue
        elif inputNumber[i] == '.' and number[i] == '#':
            continue
        else:
            return False
    return True


whatNumber = 0
for i in range(len(numbersInput)):
    candiNumber = []
    for num in numbers:
        isCandi = True
        for j in range(len(numbersInput[i])):
            # print(numbersInput[i][j], num[j], num, whatNumber)
            isSame = chkNumber(numbersInput[i][j], num[j])
            if not isSame:
                isCandi = False
                break
        if isCandi:
            candiNumber.append(whatNumber)

        whatNumber += 1
        if whatNumber >= 10:
            whatNumber = whatNumber % 9
            whatNumber = 0

    answer.append(min(candiNumber))

ans = ''
for i in range(len(answer)):
    ans += str(answer[i])
    if i == 1:
        ans += ':'

print(ans)
