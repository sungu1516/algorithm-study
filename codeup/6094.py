# 6094 : [기초-리스트] 이상한 출석 번호 부르기3

freq = int(input())
num_list = list(map(int, input().split()))

min_num = num_list[0]

for num in num_list:
    if min_num > num:
        min_num = num

print(min_num)