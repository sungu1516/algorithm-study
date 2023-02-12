def solution(strings, n):
    # lambda 함수의 인자로 튜플을 전달하여 정렬의 우선순의를 설정할 수 있음
    res = sorted(strings, key=lambda x: (x[n], x))

    return res