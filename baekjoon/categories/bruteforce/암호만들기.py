# input
l, c = map(int, input().split())
alpha = sorted(list(input().split()))   # 오름차순 정렬

# func
def isValid(password):
    consCnt = 0    # 모음
    vowCnt = 0     # 자음

    for alp in password:
        if alp in 'aeiou':
            consCnt += 1
        else:
            vowCnt += 1

    return True if consCnt >= 1 and vowCnt >= 2 else False

def go(n, password, idx):
    # 종료조건1 - 암호 길이를 만족하는 경우
    if len(password) == n:
        # 암호문의 조건을 만족하는 경우 출력
        if isValid(password):
            print(password)
        return
    # 종료조건2 - 현재 idx가 alpha 길이보다 큰 경우
    if idx >= len(alpha):
        return

    # 알파벳 선택
    go(n, password + alpha[idx], idx + 1)   # 현재 idx의 알파벳을 선택하는 경우
    go(n, password, idx + 1)   # 선택하지 않는 경우

# main
go(l, '', 0)