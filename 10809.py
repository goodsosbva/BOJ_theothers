S = input()

alphabet = [-1] * 26

# print(ord('a'))  # 97
"""
for i in S:
    #print(ord(i))
    alphabet[ord(i) - 97] += 1
"""

for i in range(len(S)):

    if alphabet[ord(S[i]) - 97] != -1:
        continue
    else:
        alphabet[ord(S[i]) - 97] = i




# print(alphabet)

#for s in alphabet:
#    print(s, end=' ')
for i in range(26):
    print(alphabet[i], end=' ')