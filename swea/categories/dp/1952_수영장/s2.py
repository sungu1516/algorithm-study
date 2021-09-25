import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    d, m1, m3, y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))

    arr = [0] * 13  # 각 월을 인덱스로, (누적)최소 비용을 값으로 갖는 배열

    arr[1] = min(plan[1]*d, m1)
    arr[2] = min(arr[1] + plan[2]*d, arr[1] + m1)

    # dp - arr 채우기
    for i in range(3, len(arr)):
        arr[i] = min(arr[i-1] + plan[i]*d, arr[i-1] + m1, arr[i-3] + m3)

    ans = min(y, arr[12])
    print('#{} {}'.format(tc, ans))