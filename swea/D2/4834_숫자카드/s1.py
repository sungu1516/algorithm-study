import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

# test case
T = int(input())

for _ in range(1, T+1):

    # 카드 개수 입력받기
    N = int(input())

    # 카드 입력받아 리스트로
    cards = [int(x) for x in input()]

    # counts list 만들기
    ## 초기화
    counts = [0] * 10

    for num in cards:
        counts[num] += 1

    # counts 리스트의 max index 구하기
    ## 초기화
    max_index = 0

    for i in range(1, len(counts)):
        if counts[max_index] <= counts[i]: # 카드 장수가 같을 때 큰 쪽을 출력하기 위해 <= 사용
            max_index = i

    # 결과 출력
    print('#{} {} {}'.format(_, max_index, counts[max_index]))