import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())        # N: 점원들의 수 / B: 선반 높이
    arr = list(map(int, input().split()))   # 점원들의 키 배열

    min_val = sum(arr)      # 최소 높이 초기화

    # 부분집합 생성
    for i in range(1 << N):
        total = 0   # 탑의 높이를 누적
        for j in range(N):
            if i & (1 << j):
                total += arr[j]
                if total > min_val: # 만약 지금까지 누적된 높이가 min_val 보다 크다면
                    break   # 해당 부분집합은 탐색 종료
        if total >= B:  # 만약 탑의 높이보다 크고, 최소값보다 작은 경우 갱신
            if total < min_val:
                min_val = total

    print('#{} {}'.format(tc, min_val - B))
