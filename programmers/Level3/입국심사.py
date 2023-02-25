def solution(n, times):
    answer = 0
    # 소요 최소시간(start), 최대시간(end) 구하기
    start = min(times)
    if n % len(times):
        end = max(times) * (n // len(times) + 1)
    else:
        end = max(times) * (n // len(times))

    # 이진탐색 진행
    while start <= end:
        mid = (start + end) // 2
        # 처리가능한 인원 수 구하기
        cnt = 0
        for time in times:
            cnt += mid // time
            if cnt >= n:
                break
        # mid time 내 처러 가능한 인원 수 >= n
        if cnt >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    # test log

    return answer