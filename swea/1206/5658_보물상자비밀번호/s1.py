import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = input()
    # 한 변당 숫자의 개수 (자리수)
    M = N // 4
    # numbers 조작
    numbers += numbers[:M-1]

    # hash 자료형인 results 에 나올 수 있는 모든 10진수 값 누적
    results = set()

    for i in range(N):
        result = int(numbers[i:i+M], 16)
        results.add(result)

    # K번째 수를 리턴하기 위해 hash -> arr로 형 변환
    results = list(results)
    # 정렬
    results.sort(reverse=True)
    # 정답
    answer = results[K-1]
    print(f'#{tc} {answer}')
