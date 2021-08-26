import sys
sys.stdin = open('input.txt')
# 함수 정의
def bfs(s, e): # 시작지점과 끝 지점을 넣어준다.
    visited = [0]*(V+1) # 방문지점
    que = [] # que
    visited[s] = 1  # 시작지점 visited, que에 넣기
    que.append(s)
    # 인접노드 탐색
    while que:
        curr = que.pop(0)  # 현재 노드
        for i in adj[curr]:
            if not visited[i]: # 방문 기록이 없을 경우
                que.append(i)
                visited[i] = visited[curr] + 1 # 출발 노드로부터의 거리 계산을 위해
                if visited[e]: # 만약 마지막 지점이 방문지점에 포함되었을 경우
                    return visited[e] - 1 # 거리 리턴

    return visited

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())    # 노드의 수, 간선의 수
    adj = [[] for _ in range(V+1)]    # 인접리스트 초기화
    # 연결노드 정보 받아서 인접리스트에 넣어주기
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1].append(n2)
        adj[n2].append(n1)

    start, end = map(int, input().split()) # 시작 노드, 도착 노드

    print(bfs(start, end))

