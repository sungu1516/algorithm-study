import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())

for _ in range(1, T + 1):
    pattern = input() # 레이저와 쇠막대기의 패턴
    cnt = 0 # 쌓인 쇠막대기의 개수
    result = 0 # 잘려진 쇠막대기 개수를 누적

    pattern = pattern.replace('()', '1') # 전처리 진행 - 레이저 '()' 에 해당하는 부분 1로 바꿔주기

    for elem in pattern: # 배열 내 모든 레이저, 쇠막대기 순회
        if elem == '1': # 레이저일 경우
            result += cnt # 현재 누적된 막대기수만큼 결과값에 더해줌
        elif elem == '(': # 쇠막대기의 시작부분일경우
            cnt += 1 # 막대기의 수를 누적한다.
            result += 1 # 결과값에 + 1
        else: # 쇠막대기의 끝 부분일 경우
            cnt -= 1 # 누적된 막대기 - 1

    print('#{} {}'.format(_, result))
