import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

for _ in range(10):
    N = int(input())
    boxes = list(map(int, input().split()))

    # 반복문을 통해 주어진 횟수만큼 평탄화 진행
    for __ in range(N):
        # 최댓값, 최솟값의 인덱스 구하기
        max_idx = 0
        min_idx = 0
        for i in range(1, 100):
            if boxes[max_idx] < boxes[i]:
                max_idx = i
            elif boxes[min_idx] > boxes[i]:
                min_idx = i

        # 해당 max, min 값에 각각 + 1, - 1 을 해준다.
        boxes[max_idx] -= 1
        boxes[min_idx] += 1

        # 만약 평탄화 작업 후 더 이상 할 필요가 없는 경우 반복문을 빠져나간다.
        if boxes[max_idx] - boxes[min_idx] <= 1:
            break

    # 모든 평탄화 작업이 종료된 후 차이값 구하기
    max_val = 0
    min_val = 100 # 문제에서 주어진 범위 조건 활용
    for box in boxes:
        if max_val < box:
            max_val = box
        elif min_val > box:
            min_val = box

    print('#{} {}'.format(_+1, max_val-min_val))