def solution(board, skill):
    destroyed = set()  # 파괴 이력이 있는 건물들의 좌표

    for arr in skill:
        command = arr[0]
        r1, c1 = arr[1], arr[2]
        r2, c2 = arr[3], arr[4]
        degree = arr[5] if command == 2 else -arr[5]

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                board[i][j] += degree
                if board[i][j] <= 0:
                    destroyed.add((i, j))

                else:
                    if (i, j) in destroyed:
                        destroyed.remove((i, j))

    result = len(board) * len(board[0]) - len(destroyed)
    return result