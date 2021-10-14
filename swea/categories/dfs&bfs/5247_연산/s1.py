import sys
sys.stdin = open('input.txt')
from collections import deque

# bfs
def bfs(s):
    que = deque([s])        # queue 초기화
    cheked = set()          # 연산의 중복을 방지

    while que:
        num, level = que.popleft()
        if num in cheked or num > 1000010: continue
        cheked.add(num)

        if num == M:       # 현재 꺼낸 값이 M과 같다면
            return level    # 거리를 리턴

        # 각 연산을 해준 후 que에 삽입
        que.append((num + 1, level + 1))
        que.append((num - 1, level + 1))
        que.append((num * 2, level + 1))
        que.append((num - 10, level + 1))

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    ans = bfs((N, 0))

    print('#{} {}'.format(tc, ans))