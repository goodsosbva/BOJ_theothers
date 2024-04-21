number = input()
number = number[::-1]
octnum = ''
for i in range(0, len(number), 3):
    num = 0
    for evol, n in enumerate(number[i:i + 3]):
        num += int(n) * (2 ** evol)  # 2진수 3묶음 => 10진수 값이자 8진수 값
        # 형태는 10진수지만 3묶음씩이므로 8을 넘어가지 않음

    octnum = str(num) + octnum  # 3묶음씩 묶어서 8진수로 만드는 전통적인 방식
print(octnum)
