number = int(input())

result = ''

if not number:
    print(0)

while number != 0:

    if number % (-2):
        result = '1' + result
        number = (number // -2) + 1
    else:
        result = '0' + result
        number //= -2

print(result)

