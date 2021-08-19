import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 필요함수 정의 - 출발점을 기준으로 방문 가능한 노드 번호를 리스트에 담아 반환
def return_visited(s, v):
    visited = [] # start node 가 방문 가능한 노드를 저장
    stack = []
    i = s # 출발점 지정
    stack.append(s) # 출발점을 먼저 스택에 쌓아준다. 출발점과 특정 노드가 이어지냐를 확인하기 때문에, 출발점을 visited 에 저장할 필요는 없음

    while stack:
        i = stack.pop() # 탐색할 노드를 스택에서 제거
        for w in range(1, v + 1): # 해당 노드 탐색 시작
            if arrs[i][w] == 1 and w not in visited: # 만약 특정 노드와 접점이 있고 해당 노드 number 가 방문지점에 없다면
                stack.append(w) # 연결된 노드를 스택에 누적
                visited.append(w) # 방문지점에도 추가

    return visited # 방문한 지점을 리턴

T = int(input())
for _ in range(1, T + 1):
    V, E = map(int, input().split())

    arrs = [[0] * (V+1) for _ in range(V+1)] # 그래프의 정보를 2차원 배열로 표현 (0으로 초기화)

    for __ in range(E): # 반복문을 활용해 입력값을 받고, 연결된 지점에 1 삽입
        n1, n2 = map(int, input().split())
        arrs[n1][n2] = 1 # arrs 중 해당 노드가 교차하는 지점에 1을 넣어준다.

    S, G = map(int, input().split()) # 출발노드, 도착노드

    visited_nodes = return_visited(S, V)
    result = 1 if G in visited_nodes else 0
    print('#{} {}'.format(_, result))


