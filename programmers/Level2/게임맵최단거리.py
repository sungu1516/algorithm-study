from collections import deque

# delta
dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)

def solution(maps):
    # 출발, 도착지점의 좌표 저장해두기
    start = (0, 0)
    n, m = len(maps), len(maps[0])

    # 출발지점 방문처리 & queue 삽입
    que = deque()
    que.append(start)
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    
    # bfs를 이용한 최단거리 탐색
    while que:
        r, c = que.popleft()
        # 도착지점인지 확인
        if (r, c) == (n - 1, m - 1):
            return visited[r][c]
        
        # 델타탐색
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            # 이동가능 인덱스 & 벽 검증
            if nr < 0 or nr >= n or nc < 0 or nc >= m or maps[nr][nc] == 0:
                continue
            # 방문여부 검증
            if not visited[nr][nc]:
                # queue 삽입 & 방문처리와 거리 기록
                que.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1
                
    # 도착지점을 찾지 못하고 while문이 종료된 경우
    return -1