list = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
sum = 0

while list:
    num = list.pop()
    if num >= 80:
        sum += num

print(sum)