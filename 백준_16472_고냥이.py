# n = int(input())

# dic = {}

# wordList = input()
# answer = 0
# l = 0
# r = 0

# while r < len(wordList):
#     if len(dic) <= n:
#         answer = max(answer, r - l)

#     if r == len(wordList):
#         break

#     if len(dic) > n:
#         tmp = 0
#         while dic[wordList[l]] > 0:
#             dic[wordList[l]] -= 1
#             tmp += 1
#         if dic[wordList[l]] == 0:
#             del dic[wordList[l]]
#         l += tmp

#     else:
#         if wordList[r] not in dic:
#             dic[wordList[r]] = 1
#             r += 1
#         else:
#             dic[wordList[r]] += 1
#             r += 1
# print(answer)

# '''
# 2
# aabbccdde
# 4

# 2
# abcde
# 2
# '''

n = int(input())
wordList = input()

dic = {}
answer = 0
l = 0
r = 0

while r < len(wordList):
    if wordList[r] in dic:
        dic[wordList[r]] += 1
    else:
        dic[wordList[r]] = 1
    
    r += 1
    
    while len(dic) > n:
        dic[wordList[l]] -= 1
        if dic[wordList[l]] == 0:
            del dic[wordList[l]]
        l += 1
    
    answer = max(answer, r - l)

print(answer)
    
    

    