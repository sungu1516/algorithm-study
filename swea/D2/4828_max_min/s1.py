import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

# test case
T = int(input())

for _ in range(1, T+1):

    # 양수의 갯수
    N = int(input())

    # 양의 정수 입력받아 리스트에 저장
    numbers = list(map(int, input().split()))

    # bubble sort로 리스트 정렬
    for i in range(N-1, 0, -1):
        for idx in range(0, i):
            if numbers[idx] > numbers[idx + 1]:
                numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]

    # 차이 구하기
    diff = numbers[-1] - numbers[0]

    print('#{} {}'.format(_, diff))
