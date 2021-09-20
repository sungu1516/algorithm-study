# delta 탐색 - 우하좌상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(row, col):      # 탐색 시작지점을 인자로 받는다.
    visited[row][col] = 1



    return

N, M = map(int, input().split())    # 도착 지점 입력받기
maze = [[int(x) for x in input()] for _ in range(N)]    # 그래프 입력받기

visited = [[[0]*M] for _ in range(N)]       # 방문지점 초기화