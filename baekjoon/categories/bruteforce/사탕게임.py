# input
N = int(input())
board = [list(input()) for _ in range(N)]

def check(arr, startRow, endRow, startCol, endCol):
    res = 1
    # row
    for i in range(startRow, endRow + 1):
        cnt = 1
        for j in range(1, N):
            if arr[i][j - 1] == arr[i][j]:
                cnt += 1
            else:
                cnt = 1

            if cnt > res:
                res = cnt

    # col
    for i in range(startCol, endCol + 1):
        cnt = 1
        for j in range(1, N):
            if arr[j - 1][i] == arr[j][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt > res:
                res = cnt

    return res

# main
maxCnt = 0
## 1. 모든 경우의 수 확인 - 인접(우, 하)칸과 swap 및 최대값 비교 & 갱신
for i in range(N):
    for j in range(N):
        # 우측칸 swap
        if j + 1 < N:
            # swap
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
            # 최대 개수 구하기 & 갱신
            cnt = check(board, i, i, j, j + 1)
            if cnt > maxCnt:
                maxCnt = cnt
            # 원복
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

        # 아래칸 swap
        if i + 1 < N:
            # swap
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
            # 최대 개수 구하기 & 갱신
            cnt = check(board, i, i + 1, j, j)
            if cnt > maxCnt:
                maxCnt = cnt
            # 원복
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]

print(maxCnt)