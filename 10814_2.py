n_members = int(input())

member_list = []
for _ in range(n_members):
    (x, y) = input().split()
    member_list.append((int(x), y))

print(member_list)
sorted_list = sorted(member_list, key=lambda k: k[0])

for i in sorted_list:
    print(i[0], i[1])

print(sorted_list)