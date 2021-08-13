import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

def search(start): # 도착지에서 위로 올라가는 함수
    i = 99 # 행
    j = start # 열
    while i>0: # 맨 윗줄에 도착하기 전까지 위로 올라감
        i -= 1 # 위로 한 칸 이동
        if j>0 and ladder[i][j-1] == 1: # 왼쪽 칸이 존재하고 1인 경우
            while j>0 and ladder[i][j-1] == 1: # 왼쪽으로 이동
                j -= 1
        elif j<99 and ladder[i][j+1] == 1: # 오른쪽 칸이 존재하고 1인 경우
            while j<99 and ladder[i][j+1] != 0: # 오른쪽 이동
                j += 1
        # 좌우가 0 이면 위로
    return j # 0번 행에 도착했을 때의 열(출발지) 리턴

T = 10 # 10개의 테스트케이스 고정
for tc in range(1, T+1):
    # test case 번호
    n = int(input())

    # 입력값으로 2차원 배열 만들기
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 도착지 검색
    goal = 0
    for i in range(100):
       if ladder[99][i] == 2:
           goal = i
    ans = search(goal)

    print('#{} {}'.format(tc, ans))