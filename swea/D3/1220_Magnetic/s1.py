import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T + 1):
    # 입력받기
    N = int(input())
    arrs = [list(map(int, input().split())) for _ in range(N)]
    stack = [] # 자성체를 담아가며 비교할 용도

    # 열방향으로 탐색
    cnt = 0 # 교착상태의 횟수를 초기화
    for j in range(N):
        for i in range(N):
            if arrs[i][j] != 0: # 빈 공간(=0)이 아닐 경우에만
                if stack: # stack 에 자성체가 존재하는 경우
                    if stack.pop() - arrs[i][j] == -1:# 만약 N극 다음에 S극이 위치하는 경우
                        cnt += 1
                    stack.append(arrs[i][j]) # 비교 후 현재 자성체를 스택에 쌓아준다.
                else:
                    stack.append(arrs[i][j])
        stack = [] # 하나의 열 탐색이 종료될 때마다 스택을 비워준다.

    print('#{} {}'.format(tc, cnt))