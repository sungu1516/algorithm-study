import sys
sys.stdin = open('input.txt')

def dfs(row, cost):
    global min_cost

    # 가지치기
    if cost >= min_cost:
        return
    # 마지막 행일 때
    if row > N - 1:
        if cost < min_cost:
            min_cost = cost
    # 제품 고르기 & 다음 행 탐색
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(row + 1, cost + arr[row][i])
            visited[i] = 0

T = int(input())
for tc in range(1, T+1):
   N = int(input())
   arr = [list(map(int, input().split())) for _ in range(N)]
   min_cost = 99 * N
   visited = [0] * N

   dfs(0, 0)

   print('#{} {}'.format(tc, min_cost))