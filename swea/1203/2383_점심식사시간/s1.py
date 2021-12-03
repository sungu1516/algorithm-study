import sys
sys.stdin = open('input.txt', 'r')

from itertools import combinations
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    exits = []      # 계단 출구의 좌표 (2개가 담길 것)
    persons = []    # 사람들의 모든 좌표가 담길 것

    # 위의 배열에 값 담아주기
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                persons.append((i, j))
            elif graph[i][j] > 1:
                exits.append((i, j))

    exit1 = exits[0]
    exit2 = exits[1]
    min_time = 987654321    # 최소 이동 시간 초기화

    # brute force - combination 을 통해, 사람들이 각각의 계단 출구에 배치되는 모든 경우의 수를 고려한다.
    for i in range(len(persons)+1):
        for comb in combinations(persons, i):
            group1 = comb   # exit1 로 나가는 사람들의 그룹
            group2 = tuple([person for person in persons if person not in group1])  # exit2 로 나가는 사람들의 그룹

            # 각 그룹의 사람이 정해진 출구에 도착하여 출발할 수 있는 시간(=도착시간 + 1분)을 담은 배열 만들기
            arrival_time1 = []
            for person in group1:
                time = abs(person[0] - exit1[0]) + abs(person[1] - exit1[1]) + 1
                arrival_time1.append(time)

            arrival_time2 = []
            for person in group2:
                time = abs(person[0] - exit2[0]) + abs(person[1] - exit2[1]) + 1
                arrival_time2.append(time)

            # 특정 그룹의 마지막 사람의 완료시간을 구한다.
            # 우선 정렬
            arrival_time1.sort()
            arrival_time2.sort()

            # 완료시간을 담을 배열을 완성한다.
            completed_time1 = []
            completed_time2 = []

            # 1번 그룹
            for i in range(len(arrival_time1)):
                if i < 3:
                    time = arrival_time1[i] + graph[exit1[0]][exit1[1]]
                    completed_time1.append(time)
                else:
                    wait = completed_time1[i-3] - arrival_time1[i]
                    if wait < 0:
                        wait = 0
                    time = arrival_time1[i] + graph[exit1[0]][exit1[1]] + wait
                    completed_time1.append(time)

            # 2번 그룹
            for i in range(len(arrival_time2)):
                if i < 3:
                    time = arrival_time2[i] + graph[exit2[0]][exit2[1]]
                    completed_time2.append(time)
                else:
                    wait = completed_time2[i-3] - arrival_time2[i]
                    if wait < 0:
                        wait = 0
                    time = arrival_time2[i] + graph[exit2[0]][exit2[1]] + wait
                    completed_time2.append(time)

            if not completed_time1:
                curr_time = max(completed_time2)
            elif not completed_time2:
                curr_time = max(completed_time1)
            else:
                curr_time = max(max(completed_time1), max(completed_time2))

            if curr_time < min_time:
                min_time = curr_time

    print(f'#{tc} {min_time}')



