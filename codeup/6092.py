# 6092 : [기초-리스트] 이상한 출석 번호 부르기1

freq = int(input())
num_list = list(map(int, input().split()))
emp_list = []

for i in range(1, 24):
    count = 0
    for num in num_list:
        if i == num:
            count += 1
    emp_list.append(count)

print(*emp_list)