import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 필요함수 정의 - 출발점을 기준으로 방문 가능한 노드 번호를 리스트에 담아 반환
def return_visited():
    visited = [0] * 100
    stack = []
    i = 0 # 출발점 설정
    visited[i] = 1

    while i != -1 and visited[99] != 1: # 하나의 경로가 끝날 때마다, visited 에 도착 노드가 있는지 확인
        for w in range(100): # 하나의 노드에 대해, 연결되는 노드들을 탐색
            if arrs[i][w] == 1 and visited[w] != 1:
                stack.append(i) # 현재 노드를 스택에 누적
                visited[w] = 1 # 다음 노드를 방문기록에 추가
                i = w # 위치 이동
                break
        # 연결된 노드가 없는 경우 - 스택에 저장된 마지막 값으로 이동하여 다시 노드 탐색
        else:
            if stack:
                i = stack.pop()
            else:
                i = -1

    return int(visited[99] == 1)

T = 10
for _ in range(1, T + 1):
    N, M = map(int, input().split())
    # 그래프 -> 2차배열 변환
    arrs = [[0] * 100 for _ in range(100)]
    ns = list(map(int, input().split()))

    for i in range(0, M*2, 2):
        n1, n2 = ns[i], ns[i+1]
        arrs[n1][n2] = 1

    print('#{} {}'.format(N, return_visited()))


