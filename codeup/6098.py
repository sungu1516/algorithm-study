# 6098 : [기초-리스트] 성실한 개미

# 입력된 값들이 들어갈 빈 배열 만들기
grid = []

# 입력값 받아서 grid list 안에 리스트 형태로 넣기
for _ in range(10):
    a_list = list(map(int, input().split()))
    grid += [a_list]

# 현재 좌표
x = 1
y = 1

# 현재위치에 9 넣어주기
grid[y][x] = 9

while True:
    # 움직일 수 없는 경우 (오른쪽, 아래 모두 장애물 존재 - 이 경우는 오른쪽 끝에 도달했을 경우도 포함)
    if grid[y+1][x] == 1 and grid[y][x+1] == 1:
        break

    # 현재 위치에서 오른쪽에 1(장애물)이 있는 경우
    elif grid[y][x+1] == 1:
        # 아래쪽으로 이동 (= 해당 칸을 9로 채워준다.)
        y += 1
        # 만약 해당 위치에 음식(2) 가 있다면?
        if grid[y][x] == 2:
            grid[y][x] = 9
            break
        grid[y][x] = 9


    # 현재 위치에서 아래에 1(장애물)이 있는 경우 or 비어있는 경우
    else:
        # 오른쪽으로 이동
        x += 1
        # 만약 해당 위치에 음식(2) 가 있다면?
        if grid[y][x] == 2:
            grid[y][x] = 9
            break
        grid[y][x] = 9

    
# 개미의 족적이 담긴 grid 출력
for a_list in grid:
    print(*a_list)