import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

# txt 파일의 10개의 test case 입력받기
for i in range(10):
    # test case 의 길이 입력받기
    case_len = int(input())
    # input 함수를 통해 입력을 받는다 : txt 파일 1줄!
    heights = list(map(int, input().split()))
    # 결과값 초기화
    result = 0

    for idx in range(2, case_len-2):
        # 비교할 높이 4개 중 최대값 구하기
        compared = [heights[idx - 1], heights[idx - 2], heights[idx + 1],  heights[idx + 2], heights[idx + 2]]
        max_val = compared[0]
        for j in range(1, len(compared) - 1):
            if compared[j] > max_val:
                max_val = compared[j]

        # test case 순회하며 조건에 맞는 경우  계산 (위에서 구한 최대값과 비교)
        if heights[idx] > max_val:
            # 각 건물단 조망권이 확보된 모든 세대를 더해준다.
            result += heights[idx] - max_val

    print('#{} {}'.format(i+1, result))