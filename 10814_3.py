n_members = int(input())

age = []
name = []
for _ in range(n_members):
    x, y = input().split()
    x = int(x)
    age.append(x)
    name.append(y)

# 나이에 따라 정렬한 인덱스값 뽑음, 나이가 정렬되지는 않음.

idx = sorted(range(len(age)), key=lambda k: age[k])
age.sort(key=lambda x: (x))


name = [name[i] for i in idx]
sorted_list = list(zip(age, name))

for i in sorted_list:
    print(i[0],i[1])

#print(sorted_list)