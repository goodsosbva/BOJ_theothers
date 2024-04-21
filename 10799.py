parenthesis = input()
count, result = 0, 0

for i in range(len(parenthesis)):
    if parenthesis[i] == "(":
        count += 1

    elif parenthesis[i] == ")" and parenthesis[i - 1] == "(":
        count -= 1
        result += count

    elif parenthesis[i] == ")":
        count -= 1
        result += 1

print(result)