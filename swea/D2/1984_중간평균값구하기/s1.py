import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))
    # 정렬 - 선택 정렬
    for i in range(0, len(numbers)-1):
        min_idx = i
        for j in range(i, len(numbers)):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    # 배열의 0번째, -1번째 값만 제외하고 평균을 구한다.
    total = 0
    for i in range(1, 9): # 입력받는 수의 개수는 정해져 있으므로
        total += numbers[i]
    mean = round(total / 8)

    print('#{} {}'.format(tc, mean))