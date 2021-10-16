import sys
sys.stdin = open('input.txt')

def dijkstra():
    dist = [987654321] * (V+1)
    visited = [0] * (V+1)

    dist[0] = 0

    for _ in range(V):
        min_idx = -1
        min_val = 987654321
        # 최소값 찾기
        for i in range(V+1):
            if not visited[i] and min_val > dist[i]:
                min_idx = i
                min_val = dist[i]

        visited[min_idx] = 1
        # 갱신할 수 있으면 갱신
        for i in range(V+1):
            if not visited[i] and dist[i] > dist[min_idx] + adj_arr[min_idx][i]:
                dist[i] = dist[min_idx] + adj_arr[min_idx][i]

    return dist[V]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_arr = [[987654321] * (V+1) for _ in range(V+1)]

    # 유향 그래프 만들기
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj_arr[s][e] = w

    print('#{} {}'.format(tc, dijkstra()))