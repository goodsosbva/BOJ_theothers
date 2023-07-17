arrList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weekList = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

month, day = map(int, input().split())
sumDay = 0

for i in range(month - 1):
    sumDay = sumDay + arrList[i]

result = (day + sumDay) % 7

print(weekList[result])

# x = arrList[month - 1]
# y = x 2 % 7
# result = weekList[y]
# print(result)