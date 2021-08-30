import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())
for tc in range(1, T + 1):
    numbers = list(map(int, input().split()))       # 7개의 정수를 담은 배열

    result = []     # 3개의 정수를 골라 합한 결과를 저장할 배열

    for i in range(7):
        for j in range(7):
            for k in range(7):
                if i != j and j != k and i != k:
                    temp = numbers[i] + numbers[j] + numbers[k]
                    if temp not in result:
                        result.append(numbers[i]+numbers[j]+numbers[k])

    result.sort(reverse=True)

    print('#{} {}'.format(tc, result[4]))