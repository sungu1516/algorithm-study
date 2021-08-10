import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

# test case 갯수 입력받기
T = int(input())

for _ in range(1, T+1):
    K, N, M = map(int, input().split())

    # 정류장, 충전소 번호가 담긴 리스트
    stop_numbers = list(range(N+1))
    charge_numbers = list(map(int, input().split()))

    # 버스의 현재 위치, 충전 횟수 초기화
    idx = 0
    cnt = 0

    # 종점까지 가는데 성공했는지 여부 - True 로 초기화
    result = True

    # 반복문을 통해 버스 이동시키기
    while True:
        if idx + K >= N:
            # 만약 현재 위치에서 충전 없이 종점까지 도착 가능하다면 반복문 나가기
            break

        if stop_numbers[idx + K] in charge_numbers:
            # 만약 (현재위치 + K) 번째 정류장에 충전소가 있다면?
            # k 만큼 위치 이동
            idx += K
            cnt += 1
        else:
            # K 만큼 떨어진 정류장에 충전소가 없다면
            # (현재위치 + K) 번째 정류장의 이전 정류장부터 현재 위치 전까지 순회하며, 가장 가까운 충전소를 찾아 이동
            for i in range(idx + K - 1, idx, -1):
                if stop_numbers[i] in charge_numbers:
                    idx = i
                    cnt += 1
                    break # 가장 가까운 충전소 찾기를 위한 반복문을 빠져나가고, 다시 버스 이동을 위한 반복문을 시행
            else:
                # for-else 문을 사용하여, 만약 이전 정류장에도 충전소가 없는 경우
                result = False # result 에 False 를 넣어주고
                break # 버스 이동을 위한 반복문 종료

    if result:
        # 종점까지 완주시 cnt 출력
        print('#{} {}'.format(_, cnt))
    else:
        # 실패 시 0 출력
        print('#{} 0'.format(_))