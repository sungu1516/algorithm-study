import sys
sys.stdin = open('input.txt', 'r')

# dfs
def dfs(person, prob):
    global max_prob

    # 가지치기
    if prob <= max_prob:
        return

    # 종료조건
    if person >= N:
        # 최대 확률 갱신
        max_prob = prob

    # 탐색
    for i in range(N):
        if not visited[i]:
            # 방문처리
            visited[i] = 1
            dfs(person + 1, prob * graph[person][i]/100)
            # 원상복구
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 최대 확률 초기화
    max_prob = 0
    # 완료한 N번째일을 기록
    visited = [0] * N

    dfs(0, 1)

    print(f'#{tc} {max_prob*100:.6f}')
