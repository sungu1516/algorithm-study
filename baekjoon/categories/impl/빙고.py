# 입력값 받기
bingo = [list(map(int, input().split())) for _ in range(5)]
answer = [list(map(int, input().split())) for _ in range(5)]

# direction : 우, 하, 좌, 상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

# bingo 판별 함수
def is_bingo(arr):
    res = False
    bingo_cnt = 0

    # 빙고 횟수 계산
    # 가로
    for i in range(5):
        is_all_zero = True
        for j in range(5):
            if arr[i][j]:
                is_all_zero = False
                break
        if is_all_zero:
            bingo_cnt += 1

    # 세로
    for i in range(5):
        is_all_zero = True
        for j in range(5):
            if arr[j][i]:
                is_all_zero = False
                break
        if is_all_zero:
            bingo_cnt += 1

    # 대각선
    is_zero_left = True # 좌상단에서 시작되는 대각선
    is_zero_right = True # 우상단에서 시작되는 대각선
    for i in range(5):
        if arr[i][i]:
            is_zero_left = False

        if arr[i][4 - i]:
            is_zero_right = False

    if is_zero_left:
        bingo_cnt += 1
    if is_zero_right:
        bingo_cnt += 1

    if bingo_cnt > 2:
        res = True
    return res

# 정답 (횟수)
cnt = 0

# 모든 정답 배열을 방문
for i in range(len(answer)):
    for j in range(len(answer[i])):
        number = answer[i][j]

        # 빙고판에서 정답 숫자의 위치를 찾는다.
        temp_val = False
        for r in range(5):
            for c in range(5):
                # 숫자와 일치하는 경우
                if number == bingo[r][c]:
                    bingo[r][c] = 0
                    temp_val = True
                    break

            if temp_val:
                break

        # 적어도 13개의 숫자를 말하는 시점부터 빙고여부 검사
        if i > 1:
            if is_bingo(bingo):
                cnt = i * 5 + (j + 1)
                break

    if cnt:
        break

print(cnt)
