# test case 의 갯수 입력받기
T = int(input())

for i in range(1, T + 1):
    # n, k 입력받기
    n, k = map(int, input().split())

    # 반복문을 통해 2차원 배열 입력받기
    row_list = []

    for _ in range(n):
        inner = list(map(int, input().split()))
        row_list.append(inner)

    # 2차원 배열의 col 값만을 리스트 단위로 가져와, 다시 리스트 안에 넣어주기
    ## 1) 필요 함수 정의- 2차원 리스트와 column 의 idx 를 인자로 넣으면 해당 위치의 col 을 리스트 형태로 리턴
    def return_col(arr_2d, col_idx):
        return [a_list[col_idx] for a_list in arr_2d]

    ## 2) 리스트 안에 넣어주기
    col_list = []
    for j in range(len(row_list)):
        col_list.append(return_col(row_list, j))

    # 0으로 padding 처리 해주기
    row_list = [[0] + a_list + [0] for a_list in row_list]
    col_list = [[0] + a_list + [0] for a_list in col_list]

    # row list 가 담긴 2차원 배열과, col list 가 담긴 2차원 배열을 각각 순회하며 개수 카운트
    result = 0
    ## 1) row list 순회하며 계산
    for a_list in row_list:
        idx = 0
        while idx <= len(a_list) - k - 2:
            # k + 2 개씩 묶어, [0, 1, 1, , ..., 0]와 같다면 결과값에 1 더해주기
            if a_list[idx:idx + k + 2] == [0] + [1] * k + [0]:
                result += 1
            idx += 1


    ## 2) col list 순회하며 계산
    for a_list in col_list:
        idx = 0
        while idx <= len(a_list) - k - 2:
            # k + 1 개씩 묶어, [0, 1, 1, , ..., 0]와 같다면 결과값에 1 더해주기
            if a_list[idx:idx + k + 2] == [0] + [1] * k + [0]:
                result += 1

            idx += 1

    print(f'#{i} {result}')