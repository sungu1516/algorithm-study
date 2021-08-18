import sys
sys.stdin = open("input.txt", "r")

# 월별 일수를 저장할 리스트 생성
cal = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
T = int(input())
for _ in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())

    if m1 == m2: # 제시된 두 월이 같은 경우
        result = d2 - d1 + 1

    else:
        result = cal[m1] - d1 + 1 # 첫 번째 날짜의 월 일수 계산
        result += d2 # 두 번째 날짜의 월 일수 계산

        # 반복문으로 나머지 일수 더해주기
        for i in range(m1+1, m2):
            result += cal[i]

    print('#{} {}'.format(_,result))
