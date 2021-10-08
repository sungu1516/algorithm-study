import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    # binary search (소요 시간 기준)
    left = 1    # 가능한 최소 소요시간
    right = max(arr) * M   # 가능한 최대 소요시간

    while left <= right:
        mid = (left + right) // 2   # 중간에 위치한 소요시간

        # 해당 시간이 주어졌을 때 심사 가능한 인원
        cnt = 0  # 인원 수
        for elem in arr:
            cnt += mid // elem  # 주어진 시간을 각 심사대별 소요시간으로 나눠준 결과를 누적

        # 만약 해당 시간이 주어진 인원을 심사하는데 부족하다면
        if cnt < M:
            left = mid + 1  # 시간을 늘린다.

        # 시간이 충분하다면
        elif cnt >= M:
            answer = mid    # 주어진 인원을 모두 심사하는 시간이므로, 일단 저장 (이후 탐색에 의해, 더 작은 값으로 최신화될 수 있음)
            right = mid - 1 # 최소 시간 탐색을 계속한다.

    print('#{} {}'.format(tc, answer))