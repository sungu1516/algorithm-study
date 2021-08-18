import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(1, T + 1):
    N = int(input())
    cnt = [0] * 10
    n = N # 결과값을 저장할 변수

    while True:
        # N 의 각 자리수 추출
        temp = n
        while temp > 0:
            cnt[temp%10] += 1
            temp //= 10
        if 0 not in cnt:  # 종료조건 : cnt 배열에 0이 없을 때까지
            break
        n += N # 아직 나오지 않은 수가 있다면 n 증가시킨 후 반복문 진행

    print('#{} {}'.format(_, n))