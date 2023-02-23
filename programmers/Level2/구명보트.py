from collections import deque

def solution(people, limit):
    answer = 0
    que = deque(sorted(people))

    while len(que) > 1:
        min_val = que[0]
        max_val = que[-1]

        if min_val + max_val <= limit:
            que.popleft()
        que.pop()
        answer += 1

    if que:
        answer += 1기
    return answer