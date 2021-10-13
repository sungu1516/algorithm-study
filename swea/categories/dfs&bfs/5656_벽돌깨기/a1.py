from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(H)]
    min_val = H*W

    def rec(depth, N, now_field):
        if depth == N:
            global min_val
            '''남아있는 벽돌의 갯수 (최소값)'''
            now_val = 0
            for i in range(H):
                for j in range(W):
                    if now_field[i][j]:
                        now_val += 1
            if now_val < min_val:
                min_val = now_val

        else:
            '''중복 순열'''
            for col_idx in range(W):
                '''벽돌 깨기'''
                new_field = [row_data[:] for row_data in now_field]     # 갖고 있는 데이터를 유지하기 위함
                que = deque()

                for row_idx, row_data in enumerate(new_field):
                    if row_data[col_idx]:
                        que.append((row_idx, col_idx, row_data[col_idx]))
                        break

                while que:
                    now_row, now_col, cnt = que.popleft()
                    # 수평
                    # now_row 변하지 X
                    # col 변함
                    # 왼쪽 범위
                    from_col = max(0, now_col - (cnt - 1))
                    # 오른쪽 범위
                    to_col = min(W - 1, now_col + (cnt - 1))

                    for next_col in range(from_col, to_col + 1):
                        if 1 < new_field[now_row][next_col]:
                            # 확산 가능성을 가진 친구를 다음에 추가
                            que.append((now_row, next_col, new_field[now_row][next_col]))
                        # 벽 깨기
                        new_field[now_row][next_col] = 0

                    # 수직
                    # now_col 변하지
                    from_row = max(0, now_row - (cnt - 1))
                    to_row = min(H - 1, now_row + (cnt -1))

                    for next_row in range(from_row, to_row + 1):
                        if 1 < new_field[next_row][now_col]:
                            que.append((next_row, now_col, new_field[next_row][now_col]))
                        # 벽 깨기
                        new_field[next_row][now_col] = 0

                # 정리
                for w in range(W):
                    real_idx = H - 1
                    for h in range(H - 1, -1, -1):
                        if not new_field[h][w]:
                            continue
                        new_field[real_idx][w], new_field[h][w] = new_field[h][w], new_field[real_idx][w]
                        real_idx -= 1

                '''재귀호출'''
                rec(depth + 1, N, new_field)

    rec(0, N, field)
    print('#{} {}'.format(tc, min_val))