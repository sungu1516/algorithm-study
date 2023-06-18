# func
def check(idx):
    s = 0
    for i in range(idx, -1, -1):
        s += ans[i]
        if signs[i][idx] == 0:
            if s != 0:
                return False
        if signs[i][idx] > 0:
            if s <= 0:
                return False
        if signs[i][idx] < 0:
            if s >= 0:
                return False

    return True

def sol(idx):
    global isSolved
    if isSolved:
        return

    # 종료조건
    if idx == n:
        isSolved = True
        # 정답 출력
        print(*ans)
        return

    # 재귀 함수 호출
    # 1) idx 위치의 숫자가 0 인 경우
    if signs[idx][idx] == 0:
        ans[idx] = 0
        if check(idx):
            sol(idx + 1)

    # 2) -, + 부호가 있는 경우
    else:
        for i in range(1, 11):
            ans[idx] = i * signs[idx][idx]
            if check(idx):
                sol(idx + 1)

# input
n = int(input())
signsStr = input()

# main
ans = [0] * n    # 정답 배열
isSolved = False # solved 여부
# 1. signs -> 2차원 배열 변환
signs = [[0] * n for _ in range(n)]
cnt = 0 # 기호에 순서대로 접근하기 위한 인덱스
for i in range(n):
    for j in range(i, n):
        if signsStr[cnt] == '0':
            signs[i][j] = 0
        elif signsStr[cnt] == '+':
            signs[i][j] = 1
        else:
            signs[i][j] = -1
        cnt += 1

# 2. 함수 실행 및 정답 출력
sol(0)
# print(*ans)