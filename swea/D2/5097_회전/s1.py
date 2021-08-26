import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 숫자의 개수, 작업 반복 수
    arr = list(input().split()) # 수열
    front = 0 # 맨 앞 숫자의 인덱스 초기화

    # 작업 반복
    for _ in range(M):
        front = (front + 1) % N

    print('#{}'.format(tc), arr[front])