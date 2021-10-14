import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    disjoint = set()  # 상호배타적인 집합의 대표 원소를 담는다.

    # 1. 새로운 집합 생성 (자기자신을 가리킴)
    p = list(range(N+1))

    # 2. 대표 원소를 변경
    for i in range(M):
        p[arr[2*i+1]] = arr[2*i]
    
    # 3. 상호배타적 집합의 원소 개수
    for i in range(1, N+1):
        while i != p[i]:
            i = p[i]
        disjoint.add(i)

    print('#{} {}'.format(tc, len(disjoint)))