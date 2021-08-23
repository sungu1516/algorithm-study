import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split()) # 최대거리, 정류장 갯수, 충전소 갯수
    stops = list(range(N+1))
    charges = list(map(int, input().split()))
    cnt = 0 # 충전횟수
    i = 0 # 위치

    while i + K < N:
        ni = i + K # 다음 위치를 저장

        if ni in charges:
            i = ni # 실제 이동
            cnt += 1 # 충전 횟수 ++

        else:
            for j in range(ni-1, i, -1):
                if j in charges:
                    i = j # 해당 위치로 이동
                    cnt += 1
                    break
            else:
                break

    if i + K >= N:
        result = cnt
    else:
        result = 0
    print('#{} {}'.format(tc, result))