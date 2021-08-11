import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

for _ in range(1, 11):
    # test case 의 번호 입력받기
    T = int(input())
    
    # 100 * 100 배열 만들기
    arrs = [list(map(int, input().split())) for _ in range(100)]

    # 배열의 각 행, 열, 대각선의 합을 담을 리스트
    result = []

    # row
    for i in range(100):
        result.append(sum(arrs[i]))

    # column
    for j in range(100):
        # 각 열의 숫자를 더한 값 초기화
        column = 0
        for i in range(100):
            column += arrs[i][j]
        result.append(column)

    ## 우하향 대각선
    down_right = 0
    for i in range(0, 100):
        down_right += arrs[i][j]
    result.append(down_right)

    ## 좌하향 대각선
    down_left = 0
    for i in range(0, 100):
        down_left += arrs[i][99-i]
    result.append(down_left)

    # 결과 중 최대값 출력
    print('#{} {}'.format(_, max(result)))
