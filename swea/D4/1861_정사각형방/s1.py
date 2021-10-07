import sys

sys.stdin = open('input.txt')
# delta
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]   # 탐색과정에서 이동했던 숫자를 기록
    max_ans = (N**2+1, 0)   # 숫자, 이동 횟수를 저장한다.

    # 모든 방으로부터 출발
    for i in range(N):
        for j in range(N):
            if visited[i][j]: continue  # 가지치기 - 만약 과거 탐색과정에서 이미 방문한 방이면 지나간다.
            r, c = i, j
            cnt = 1

            # 탐색
            able = 1   # 이동 가능 여부
            while able:
                for k in range(4):
                    nr, nc = r + dr[k], c + dc[k]
                    if 0 <= nr < N and 0 <= nc < N:
                        if graph[r][c] + 1 == graph[nr][nc]:
                            visited[nr][nc] = 1
                            r = nr
                            c = nc
                            cnt += 1
                            break
                # 주면에 이동할 곳을 찾지 못하고 끝난 경우
                else:
                    able = 0

            # 최댓값 비교 후 갱신
            if cnt > max_ans[1]:
                max_ans = (graph[r][c] - cnt + 1, cnt)
            elif cnt == max_ans[1]:
                if graph[r][c] < max_ans[0]:
                    max_ans = (graph[r][c] - cnt + 1, cnt)

    print('#{} {} {}'.format(tc, *max_ans))
