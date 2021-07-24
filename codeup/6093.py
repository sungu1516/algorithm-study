# 6093 : [기초-리스트] 이상한 출석 번호 부르기2

freq = int(input())
num_list = list(map(int, input().split()))

for i in range(freq - 1, -1, -1):
    print(num_list[i], end=' ')