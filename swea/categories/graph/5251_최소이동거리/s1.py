import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[0] * (V+1) for _ in range(V+1)]
    checked = [0] * (V+1)

    # 유향 그래프 만들기
    for _ in range(E):
        s, e, w = map(int, input().split())
        arr[s][e] = w

    distance = [987654321] * (V+1)
    distance[0] = 0

    for _ in range(V):
        # distance 배열 중 최소값을 찾는다
        min_idx = 0
        min_val = 987654321
        for i in range(V+1):
            if (distance[i] < min_val) and not checked[i]:
                min_val = distance[i]
                min_idx = i

        # 방문처리
        checked[min_idx] = 1

        # 해당 지점을 기준으로 각 지점까지의 최소거리 갱신
        for i in range(V+1):
            if arr[min_idx][i]:
                cum_dist = distance[min_idx] + arr[min_idx][i]
                if cum_dist < distance[i]:
                    distance[i] = cum_dist


    print('#{} {}'.format(tc, distance[V]))