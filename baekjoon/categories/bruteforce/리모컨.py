# 입력값
ch = int(input())
n = int(input())
btnArr = list(map(int, input().split()))    # 고장난 버튼 배열

# dfs
def dfs(strNum):
    global min_cnt
    # 종료조건
    if len(strNum) == len(str(ch)):
        # 버튼 누르는 횟수 구하기
        cnt = abs(int(strNum) - ch) + len(strNum)
        # 갱신
        if cnt < min_cnt:
            min_cnt = cnt
    # 목표한 채널의 자리수와 동일한 경우
    pass

# main
min_cnt = ch # 최소 횟수 초기화
tmpCh = ''

# 목표 채널의 각 자릿수를 순회
for strNum in str(ch):
    # 해당 자리수 버튼이 고장나지 않은 경우
    if strNum not in btnArr:
        dfs(tmpCh + strNum)
        continue

    # 해당 자리수 버튼이 고장난 경우
    # 재귀 호출 - 0 ~ 9 숫자 중 고장나지 않은 숫자인 경우
    for i in range(9):
        if i not in btnArr:
            # 현재까지 완성된 자리수를 인자로 넣어준다.
            dfs(tmpCh + str(i))
