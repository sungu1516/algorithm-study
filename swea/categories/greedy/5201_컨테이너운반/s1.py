import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 무게 & 적재 용량 받기 - 정렬해준다.
    loads = sorted(list(map(int, input().split())))
    trucks = sorted(list(map(int, input().split())), reverse=True)
    max_w = 0   # 최대용량 초기화

    # 최대 용량 구하기
    for w in trucks:    # 트럭(적재용량)을 하나하나 순회하며
        if not loads:   # 화물을 모두 꺼낸 경우
            break
        while loads:
            load_w = loads.pop()    # 화물 꺼내기
            if w >= load_w:      # 적재 가능하다면
                max_w += load_w
                break

    print('#{} {}'.format(tc, max_w))