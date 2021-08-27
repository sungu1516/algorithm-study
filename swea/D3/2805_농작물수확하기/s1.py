import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    farm = [[int(x) for x in list(input())] for _ in range(N)] # 농장

    total = 0    # 농장 수익 초기화
    # 농장의 첫 번째 (큰)삼각형의 수익 구하기
    idx = 0
    for row in farm:
        if len(row[N//2-idx:N//2+1+idx]) == N:
            total += sum(row[N // 2 - idx:N // 2 + 1 + idx])
            break
        total += sum(row[N//2-idx:N//2+1+idx])
        idx += 1

    # 농장의 두 번째 삼각형의 수익 구하기
    idx2 = 0
    for i in range(N-1, 0, -1):
        if len(farm[i][N//2-idx2:N//2+1+idx2]) == N:
            break
        total += sum(farm[i][N//2-idx2:N//2+1+idx2])
        idx2 += 1

    print('#{} {}'.format(tc, total))


