S = input()

alphabet = [0] * 26
#print(ord('a'))  # 97
#print(len(S))

for i in S:
    #print(ord(i))
    alphabet[ord(i) - 97] += 1


#print(alpabet)

for s in alphabet:
    print(s, end=' ')
