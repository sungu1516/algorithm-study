# 6083 : [기초-종합] 빛 섞어 색 만들기

r_num, g_num, b_num = map(int, input().split())

for r in range(0, r_num):
    for g in range(0, g_num):
        for b in range(0, b_num):
            print(r, g, b)

print(r_num * g_num * b_num)