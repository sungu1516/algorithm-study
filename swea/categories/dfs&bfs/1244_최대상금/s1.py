import sys
sys.stdin = open('input.txt', 'r')

def dfs(arr, idx, cnt):
    global max_reward
    if cnt == M:    # 주어진 횟수만큼 자리 변경을 완료했다면
        # 최대값 비교 & 갱신
        reward = int(''.join(arr))  # int로 변환
        # max_reward 와 비교
        if reward > max_reward:
            max_reward = reward
        return

    # 조합 - 인덱스 선택 후 내림차순 정렬
    for i in range(idx, len(arr)-1):
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:  # 뒤의 숫자가 더 큰 경우
                arr[i], arr[j] = arr[j], arr[i] # 자리 이동
                dfs(arr, i, cnt+1)  # 자리이동했으므로 cnt ++ / i번째 자리까지 내림차순 정렬이 안되었으므로, i를 인자로 다시 넣어준다.
                arr[i], arr[j] = arr[j], arr[i]     # 원상복구

T = int(input())
for tc in range(1, T+1):
    numbers, M = map(int, input().split())  # 숫자판, 교환횟수
    numbers = list(str(numbers))   # 배열로 변환
    max_reward = 0

    dfs(numbers, 0, 0)
    print('#{} {}'.format(tc, max_reward))

