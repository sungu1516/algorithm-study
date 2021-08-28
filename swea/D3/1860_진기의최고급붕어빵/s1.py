import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())
for tc in range(1, T + 1):
    print('#{}'.format(tc), end = ' ')
    N, M, K = map(int, input().split())     # 받은 손님 수, 필요 시간(초), 만드는 붕어빵의 개수
    customers = list(map(int, input().split()))     # 손님정보(몇 초에 방문하는지)

    # 방문하는 시간(초)를 인덱스로 가지고, 방문하는 손님 수를 값으로 가지는 배열 생성
    reserve = [0] * (max(customers) + 1)
    for i in customers:
        reserve[i] += 1

    fish = 0    # 붕어빵 개수 초기화
    sec = 0     # 시간 초기화

    while sec < len(reserve) and fish >= 0:        # 종료조건 : 마지막 손님까지 받거나, 붕어빵이 부족하거나
        if sec % M == 0 and sec:
            fish += K       # 초당 만들 수 있는 붕어빵을 추가

        fish -= reserve[sec]  # 해당 초에 방문하는 고객의 수만큼 붕어빵을 --
        sec += 1            # 시간이 흐른다.

    if fish < 0:
        print('Impossible')
    else:
        print('Possible')
