n = int(input())
agearr = []
namearr = []
#dir = {}


for i in range(n):
    a, b = input().split()    # 입력받은 값을 공백을 기준으로 분리
    a = int(a)

    agearr.append(a)
    namearr.append(b)
    #dir[i] = [a, b]

#for age, name in agearr:
    #dir[age] = name
# print(twoDimension)
# print(type(twoDimension[0][1]))

#a = [0, 1, 2]
agearr.sort(key=lambda x: (x))  # 중요 부분
index = sorted(range(len(agearr)), key=lambda k: agearr[k])
#print(len(index))
#print(len(a))
#print(index)
#print(a)
namearr = [namearr[i] for i in index]
#print(agearr)

sorted_list = list(zip(agearr, namearr))

#print(agearr)
#dir.sort(key=lambda x: (x[1][0], x[0]))

#print(namearr)


#for i in agearr:
#    print(i[0], i[1])  # 이런식으로 프린트 할 수 도있다. 알아둘것.

for i in sorted_list:
    print(i[0], i[1])

