def solution(N, stages):
    answer = []
    result = []

    # 1. 각 스테이지 번호와 실패율을 가진 배열 완성
    # for : 1 ~ N
    for i in range(1, N + 1):
        denom = 0  # 실패율 계산을 위한 분모
        numer = 0  # 실패율 계산을 위한 분자
        # for : stages
        for stage in stages:
            if i <= stage:
                denom += 1
            if i == stage:
                numer += 1

        # 분모값이 0인지 판단
        if (denom == 0):
            fail_rate = 0
        else:
            fail_rate = numer / denom

        # (index, fail_rate) 배열에 담기
        result.append((i, fail_rate))

    # 2. 정렬하기
    result.sort(reverse=True, key=lambda x: x[1])

    for i in range(len(result)):
        answer.append(result[i][0])

    return answer