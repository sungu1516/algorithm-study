import sys
sys.stdin = open('input.txt')

# test case
T = int(input())

for _ in range(1, T+1):
    N = int(input())
    # 인수들을 담은 리스트
    numbers = [2, 3, 5, 7, 11]

    # a,b,c,d,e 값을 담을 리스트 초기화
    result = [0] * 5

    # numbers를 순회할 인덱스를 초기화
    idx = 0

    # 반복문을 통해 결과값을 저장
    while N > 1:
        if N % numbers[idx] == 0:
            # 만약 N을 특정 인수로 나누었을 때, 나머지가 0인 경우
            result[idx] += 1 # result 리스트의 해당 인덱스 자리에 1을 더해준다.

            # N 의 값에 해당 인수로 나눠준 몫을 저장한 후, 계속 진행
            N = N // numbers[idx]
            continue

        # 만약 나머지가 0이 아닌 경우 인덱스값을 더해주고 다음 인수로 반복문 진행
        idx += 1

    # 결과 출력
    print('#{} {} {} {} {} {}'.format(_, *result))