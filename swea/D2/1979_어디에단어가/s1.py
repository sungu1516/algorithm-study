import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]

    # 단어가 들어갈 수 있는 자리의 수 초기화
    cnt = 0

    # 반복문 통해 2차원 배열의 모든 행에 대해 탐색
    for row in arr:
        for i in range(0, len(arr)-K+1):
            if row[i:i+K+2] == [0] + [1]*K + [0]: # 만약 행의 특정 부분이 [0, 1, 1, 1, 0] 과 같다면
                cnt += 1

    # 90도 회전한 2차원 배열 새로 만들기 for 열 탐색
    arr2 = []
    for j in range(1, N + 1): # 위에서 패딩한 것을 고려하여 range 설정
        col = []
        for i in range(N):
            col.append(arr[i][j])
        arr2.append([0] + col + [0]) # 동일한 방식으로 패딩

    # 반복문 통해 모든 열에 대해 탐색
    for row in arr2:
        for i in range(0, len(arr) - K + 1):
            if row[i:i + K + 2] == [0] + [1] * K + [0]:  # 만약 행의 특정 부분이 [0, 1, 1, 1, 0] 과 같다면
                cnt += 1

    print('#{} {}'.format(_, cnt))


