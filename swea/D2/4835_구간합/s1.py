import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

# test case
T = int(input())

for _ in range(1, T+1):

    # 정수의 개수, 구간의 개수 입력받기
    N, M = map(int, input().split())

    # 정수 리스트 입력받기
    arr = list(map(int, input().split()))

    # 리스트 순회하며 구간합 결과 result 에 담기
    result = []

    for i in range(0, N-M+1):
        total = 0
        for j in range(i, i+M):
            total += arr[j]
        result.append(total)

    # 구간합 결과인 result 를 정렬

    # bubble sort 이용
    for i in range(len(result)-1, 0, -1):
        for idx in range(0, i):
            if result[idx] > result[idx + 1]:
                result[idx], result[idx + 1] = result[idx + 1], result[idx]

    # 정렬된 배열내 요소의 최댓값 - 최솟값
    difference = result[-1] - result[0]

    print('#{} {}'.format(_, difference))