n, k = list(map(int, input().split()))

numbers = list(map(int, input().split()))
prefix = 0
dic = {}
dic[0] = 1

answer = 0
for n in numbers:
    prefix += n

    if dic.get(prefix - k, 0) != 0:
        answer += dic[prefix - k]
    dic[prefix] = dic.get(prefix, 0) + 1

print(answer)