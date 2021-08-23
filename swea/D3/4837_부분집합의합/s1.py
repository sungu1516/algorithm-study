import sys
sys.stdin = open('input.txt', encoding='UTF-8')

A = list(range(1, 13))
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split()) # 원소의 개수, 합
    cnt = 0 # 조건에 맞는 부분집합의 개수

    for i in range(1<<len(A)):
        temp = []
        for j in range(len(A) + 1):
            if i & (1<<j):
                temp.append(A[j])
        if len(temp) == N and sum(temp) == K:
            cnt += 1

    print('#{} {}'.format(tc, cnt))