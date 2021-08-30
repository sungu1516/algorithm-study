import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 함수정의
def get_hour(day, hour, minute):
    if minute < 0:
        hour -= 1
        minute += 60
    if hour < 0:
        day -= 1
        hour += 24
    if day < 0:
        return -1

    result = day*24*60 + hour*60 + minute
    return result

T = int(input())
for tc in range(1, T + 1):
    D, H, M = map(int, input().split())
    D, H, M = D - 11, H - 11, M - 11
    ans = get_hour(D, H, M)
    print('#{} {}'.format(tc, ans))

