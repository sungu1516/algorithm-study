from collections import deque

# 우하좌상
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)


# bfs 활용
def is_far(graph):
    # 모든 응시자들의 위치에 대해 확인
    for r in range(5):
        for c in range(5):
            if graph[r][c] == 'P':
                # BFS
                visited = [[0] * 5 for _ in range(5)]   # 방문 표시 겸 거리 표시
                que = deque([(r, c)])
                visited[r][c] = 1
                # que가 빌 때까지 원소 꺼내서 상하좌우 탐색
                while que:
                    cr, cc = que.popleft()
                    # 상하좌우 탐색
                    for k in range(4):
                        nr, nc = cr + dr[k], cc + dc[k]
                        # 인덱스 범위 외부에 있는 경우 - continue
                        if nr < 0 or nr >= 5 or nc < 0 or nc >= 5 or visited[nr][nc]: continue
                        # 만약 상하좌우 인접자리에 또 다른 응시자가 존재하는 경우
                        if graph[nr][nc] == 'P': return 0

                        # 만약 해당 좌표가 빈자리인 경우 - que에 담아준다.
                        # 응시자 좌표에서 2칸 떨어진 좌표는 que에 담을 필요가 없으므로, visited 배열을 이용하여 조건 처리
                        if visited[cr][cc] < 2 and graph[nr][nc] == 'O':
                            visited[nr][nc] = visited[cr][cc] + 1
                            que.append((nr, nc))
    # 모든 응시자 좌석이 조건을 만족하는 경우
    return 1


def solution(places):
    answer = []

    # 모든 place를 순회한다.

    for place in places:
        answer.append(is_far(place))

    return answer

p = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(p))