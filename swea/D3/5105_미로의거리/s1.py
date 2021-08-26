import sys
sys.stdin = open('input.txt')
# 델타탐색
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 함수 정의
def bfs(start): # 시작지점의 인덱스를 배열로 넣어줌
    visited = [[0]*(N) for _ in range(N)] # 방문지점을 2차원 배열로 만들어준다. 이후 특정 지점과 출발노드간의 거리를 계산하는데 활용
    que = [] # que
    visited[start[0]][start_node[1]] = 1 # 출발노드의 방문지에 1을 넣어줌
    que.append(start)
    k = 0 # 델타탐색을 위한 인덱스 초기화

    # 인접노드 탐색
    while que:
        curr = que.pop(0)  # 현재 위치한 인덱스([i, j])
        for k in range(4): # 델타탐색 활용
            i, j = curr[0] + di[k], curr[1] + dj[k] # 상, 우, 하, 좌 순으로 모두 탐색해본다.

            if 0 <= i < N and 0 <= j < N and maze[i][j] == 3 and not visited[i][j]: # 인덱스가 범위안에 있고, 도착지를 발견?
                return visited[curr[0]][curr[1]] - 1 # 도착노드까지의 거리(이전 노드까지의 탐색 횟수 - 1) 를 리턴

            elif 0 <= i < N and 0 <= j < N and maze[i][j] == 0 and not visited[i][j]: # 3을 발견하진 못했지만 연결된 경우
                visited[i][j] = visited[curr[0]][curr[1]] + 1 # 방문지점에 노드 거리를 누적
                que.append([i, j])

    return 0 # 만약 도착 지점을 찾지 못한다면


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [[int(x) for x in input()] for _ in range(N)] # 2차원 배열의 미로

    # 출발지점을 찾아 배열형태로 저장
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start_node = [i, j]
                break

    # 함수 실행 및 출력
    print('#{}'.format(tc), end= ' ')
    print(bfs(start_node))

