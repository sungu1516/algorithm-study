# 6096 : [기초-리스트] 바둑알 십자 뒤집기

# 입력받기

# 2차원 배열 생성
grid = []

for _ in range(19):
    grid.append(list(map(int, input().split())))

# 좌표값 입력받기
cnt = int(input())
# 입력받은 횟수만큼 좌표를 받아, 코드 수행
for _ in range(cnt):
    y, x = map(int, input().split())
    # 리스트 조작의 편의를 의해, 좌표값 변경
    x, y = x - 1, y - 1

    # 반복문 통해 해당 좌표 기준으로 값 변경
    # 가로줄 뒤집기
    grid[y] = [int(not bool(stone)) for stone in grid[y]] 
    # 세로줄 뒤집기
    for a_list in grid:
        a_list[x] = int(not bool(a_list[x]))


for a_list in grid:
    print(*a_list)