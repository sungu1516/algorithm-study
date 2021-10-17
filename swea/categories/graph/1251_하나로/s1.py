import sys
sys.stdin = open('input.txt')

# prim
def prim():
    key = [float('inf')] * N
    visited = [0] * N
    key[0] = 0

    for _ in range(N-1):
        min_idx = -1
        min_val = float('inf')
        # 최소값 탐색
        for i in range(N):
            if not visited[i] and key[i] < min_val:
                min_idx = i
                min_val = key[i]

        visited[min_idx] = 1
        # 최소 비용을 갱신
        for i in range(N):
            if not visited[i] and adj_arr[min_idx][i] < key[i]:
                key[i] = adj_arr[min_idx][i]

    return round(E * sum(key))

T = int(input())
for tc in range(1, T+1):
    N = int(input())        # 섬의 개수
    X = list(map(int, input().split()))   # 각 섬의 X좌표
    Y = list(map(int, input().split()))   # 각 섬의 Y좌표
    E = float(input())

    # adj_arr 완성
    adj_arr = [[0] * N for _ in range(N)]   # 각 지점까지의 비용 초기화
    for i in range(N):
        for j in range(N):
            adj_arr[i][j] = ((X[i] - X[j])**2 + (Y[i] - Y[j])**2)

    print('#{} {}'.format(tc, prim()))