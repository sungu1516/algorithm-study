from collections import deque
def solution(rows, columns, queries):
    '''
    rows랑 cols 받아서 2차원 배열로 만드는 과정에서 실수가 많았다...
    2차원 배열이 제대로 만들어졌는지 확인도 안한채 다른 곳에서 에러 발생 원인을 찾아서, 시간을 너무 많이 쓰게 되었다.
    '''
    # 0. 입력값으로 배열 만들기

    graph = []
    for i in range(0, rows):
        graph.append(list(range(i*columns + 1, i*columns + columns + 1)))

    # result (최소값을 담는다)
    result = []

    for query in queries:
        # 좌표값
        x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1

        # delta - 우하좌상
        dr = (0, 1, 0, -1)
        dc = (1, 0, -1, 0)

        # 최소값 초기화
        min_val = 10000

        # 1. delta를 이용하여 지정된 범위의 원소 시계방향으로 회전
        # 좌상단 원소부터 시작
        i = 0  # delta 이동 방향 초기화
        now_row, now_col = x1, y1  # 현재 위치한 좌표 (출발지점)
        next_row, next_col = now_row + dr[i], now_col + dc[i]  # 다음으로 확인할 좌표
        que = deque()    # 회전을 위한 que

        # 출발지점까지 다시 돌아올 때까지 delta 탐색하며 회전
        while (next_row, next_col) != (x1-1, y1):
            # 만약 다음 좌표가 회전 범위 내에 있다면
            if x1 <= next_row <= x2 and y1 <= next_col <= y2:
                # que 가 비어있는 경우
                if not que:
                    que.append(graph[next_row][next_col])
                    graph[next_row][next_col] = graph[now_row][now_col]
                else:
                    que.append(graph[next_row][next_col])
                    graph[next_row][next_col] = que.popleft()

                # 최소값 갱신
                if graph[next_row][next_col] < min_val:
                    min_val = graph[next_row][next_col]

            # 범위를 벗어나는 경우
            else:
                i += 1  # 이동방향 변경
                next_row, next_col = now_row, now_col

            # 현재좌표 갱신
            now_row, now_col = next_row, next_col

            # next 좌표 갱신
            next_row += dr[i]
            next_col += dc[i]

        # 최소값을 result에 담아둔다.
        result.append(min_val)

    return result

print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))