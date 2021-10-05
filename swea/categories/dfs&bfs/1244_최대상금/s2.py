import sys
sys.stdin = open('input.txt', 'r')

def dfs(arr, cnt):
    global max_reward
    reward = int(''.join(arr))  # int로 변환

    if (reward, cnt) in records:    # 가지치기 - 이전에 동일한 변경횟수에 대해 같은 숫자가 존재하는 경우
        return

    records.add((reward, cnt))      # 변경횟수와 reward 를 기록해둔다.

    if cnt == M:    # 주어진 횟수만큼 자리 변경을 완료했다면
        # 최대값 비교 & 갱신
        if reward > max_reward:
            max_reward = reward
        return

    # 변경횟수가 남은 경우 - 자리 선택
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            # 자리 바꿈
            arr[i], arr[j] = arr[j], arr[i]
            # 자리를 바꾼 후 한층 더 탐색
            dfs(arr, cnt+1)
            # 원상복구
            arr[i], arr[j] = arr[j], arr[i]

T = int(input())
for tc in range(1, T+1):
    numbers, M = map(int, input().split())  # 숫자판, 교환횟수
    numbers = list(str(numbers))   # 배열로 변환
    max_reward = 0
    records = set()     # 이미 탐색한 reward 를 저장해둔다.

    dfs(numbers, 0)
    print('#{} {}'.format(tc, max_reward))

