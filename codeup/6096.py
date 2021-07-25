# 6096 : [기초-리스트] 바둑알 십자 뒤집기

# 바둑판과 같은 2차원 리스트 만들기
badukpan = []
for _ in range(19):
    inner_list = []
    for _ in range(19):
        inner_list.append(0)
    badukpan.append(inner_list)

# 입력 받기
number = int(input()) # 바둑알 개수

for _ in range(number): # 위에서 입력받은 개수만큼 반복하며 특정 좌표에 1삽입
    x, y = map(int, input().split(' '))
    badukpan[x - 1][y - 1] = 1

# 출력
for row in badukpan:
    for el in row:
        print(el, end = ' ')
    print()