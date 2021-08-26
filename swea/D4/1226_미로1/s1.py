import sys
sys.stdin = open('input.txt')
# 델타탐색
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 함수 정의
def bfs(start): # 시작지점의 인덱스를 배열로 넣어줌
    visited = [[0]*(16) for _ in range(16)] # 방문지점을 2차원 배열로 만들어준다
    que = [] # que
    visited[start[0]][start_node[1]] = 1 # 방문기록
    que.append(start)
    k = 0 # 델타탐색을 위한 인덱스 초기화

    # 인접노드 탐색
    while que:
        curr = que.pop(0)  # 현재 위치한 인덱스([i, j])
        for k in range(4): # 델타탐색 활용
            i, j = curr[0] + di[k], curr[1] + dj[k] # 상, 우, 하, 좌 순으로 모두 탐색해본다.

            if 0 <= i < 16 and 0 <= j < 16 and maze[i][j] == 3 and not visited[i][j]: # 인덱스가 범위안에 있고, 도착지를 발견?
                return 1
            elif 0 <= i < 16 and 0 <= j < 16 and maze[i][j] == 0 and not visited[i][j]: # 도착지를 발견하진 못했지만 연결된 경우
                visited[i][j] = 1 # 방문 표시
                que.append([i, j])

    return 0 # 만약 도착 지점을 찾지 못한다면


T = 10
for tc in range(1, T+1):
    tc = input()
    maze = [[int(x) for x in input()] for _ in range(16)] # 2차원 배열의 미로

    # 출발지점
    start_node = [1, 1]

    # 함수 실행 및 출력
    print('#{} {}'.format(tc, bfs(start_node)))
