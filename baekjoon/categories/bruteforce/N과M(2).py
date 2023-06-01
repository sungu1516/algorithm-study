# input
n, m = map(int, input().split())

# func
def perm(idx, selected, n, m):
    # 종료조건1
    if selected == m:
        print(*arr)
        return

    # 종료조건2
    if idx > n:
        return

    # 재귀방문
    # 1. 현재 idx의 숫자를 선택하는 경우
    arr[selected] = idx
    perm(idx + 1, selected + 1, n, m)
    # 원복
    arr[selected] = 0
    # 2. 선택하지 않는 경우
    perm(idx + 1, selected, n, m)

# main
arr = [0 for _ in range(m)]  # 선택된 숫자 기록
perm(1, 0, n, m)